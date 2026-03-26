from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team 2', description='Another test team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team, is_superhero=False)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team 3', description='Another test team')
        user = User.objects.create(email='test2@example.com', username='testuser2', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Running', duration_minutes=20, date='2026-03-26')
        self.assertEqual(activity.activity_type, 'Running')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team 4', description='Another test team')
        workout = Workout.objects.create(name='Test Workout', description='A workout')
        workout.suggested_for.set([team])
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team 5', description='Another test team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(leaderboard.total_points, 100)
