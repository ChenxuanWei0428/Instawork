from django.test import TestCase
from .models import TeamMember


class TeamMemberModelTest(TestCase):
    def setUp(self):
        # Create a test team member
        self.team_member = TeamMember.objects.create(first_name='Chenxuan', 
                                                     last_name="Wei", 
                                                     role='admin', 
                                                     email="test@gmail.com", 
                                                     phone_number="1234567890")

    def test_team_member_creation(self):
        # Test if the team member is created correctly
        self.assertEqual(self.team_member.first_name, 'Chenxuan')
        self.assertEqual(self.team_member.last_name, "Wei")
        self.assertEqual(self.team_member.email, "test@gmail.com")
        self.assertEqual(self.team_member.phone_number, "1234567890")
        self.assertEqual(self.team_member.role, 'admin')
        