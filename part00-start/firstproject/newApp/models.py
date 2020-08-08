from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GAME_STATUS_CHOICES =(
	('A', 'active'),
	('x', 'p0 won'),
	('y', 'p1 won')
)
class Game(models.Model):
	player0 = models.ForeignKey(User, related_name = 'p0', on_delete=models.CASCADE)
	player1 = models.ForeignKey(User, related_name = 'p1', on_delete=models.CASCADE)
	next_to_move = models.ForeignKey(User, related_name = 'nextToMove', on_delete=models.CASCADE)
	start_time = models.DateTimeField(auto_now_add = True)
	last_active = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 1, default = 'A',
					choices = GAME_STATUS_CHOICES)

	def __str__(self):
		return f'{self.player0} against {self.player1}'

class Move(models.Model):
	x = models.IntegerField()
	y = models.IntegerField()
	comment = models.CharField(max_length = 300)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)