from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            User(email='tony@marvel.com', username='IronMan', team=marvel, is_superhero=True),
            User(email='steve@marvel.com', username='CaptainAmerica', team=marvel, is_superhero=True),
            User(email='bruce@marvel.com', username='Hulk', team=marvel, is_superhero=True),
            User(email='clark@dc.com', username='Superman', team=dc, is_superhero=True),
            User(email='bruce@dc.com', username='Batman', team=dc, is_superhero=True),
            User(email='diana@dc.com', username='WonderWoman', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        users = list(User.objects.all())
        activities = [
            Activity(user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now().date()),
            Activity(user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now().date()),
            Activity(user=users[2], activity_type='Swimming', duration_minutes=60, date=timezone.now().date()),
            Activity(user=users[3], activity_type='Flying', duration_minutes=120, date=timezone.now().date()),
            Activity(user=users[4], activity_type='Martial Arts', duration_minutes=90, date=timezone.now().date()),
            Activity(user=users[5], activity_type='Lasso Training', duration_minutes=50, date=timezone.now().date()),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        workout2 = Workout.objects.create(name='Flight Training', description='Flight skills for superheroes')
        workout1.suggested_for.set([marvel, dc])
        workout2.suggested_for.set([dc])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=300)
        Leaderboard.objects.create(team=dc, total_points=350)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
