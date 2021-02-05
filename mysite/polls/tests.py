from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question
from django.urls import reverse


def create_questions(question_text, days):
    """
    Cria uma questão com o texto dado and publica de acordo com o número de diferença em relação ao dia atual passado,
    (negativo para passado e positivo para futuro)
    """
    time = timezone.now() - datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        :return: false, for questions whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        :return: False for questions whose pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        :return: True for questions whose pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewsTests(TestCase):
    def test_no_questions(self):
        """
        se não existir questão, uma mensagem apropriada é mostrada
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        create_questions(question_text="Past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], ["<Question: Past question>"]
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page
        """
        create_questions(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Mesmo se existirem questões do passado e do futuro, apenas as do passado são mostradas
        """
        create_questions(question_text="Past question", days=-30)
        create_questions(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            ["<Question: Past question>"]
        )

    def test_two_past_questions(self):
        """
        Mostra varias questões, e em ordem
        """
        create_questions(question_text="Past question 1", days=-30)
        create_questions(question_text="Past question 2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            ["<Question: Past question 2>", "Question: Past question 1>"]
        )


class QuestionDetailsViewTests(TestCase):
    def test_future_question(self):
        """
        Para uma visualização de uma questão no futuro, o site deve retornar 404
        """
        future_question = create_questions(question_text="Future question", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Para uma questão no passado, a view detail mostra o texto
        """
        past_question = create_questions(question_text="Past question", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)