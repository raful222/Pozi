from django.test import TestCase
from django.urls import reverse, resolve
from chat.views import Inbox,cost_chat,UserSearch,Directs,SendDirect,Inbox_cost,Daliy_Tip


class Test_url(TestCase):
    def test_Inbox(self):
        url = reverse('chat:Inbox')
        self.assertEqual(resolve(url).func, Inbox)

    def test_cost_chat(self):
        url = reverse('chat:cost_chat')
        self.assertEqual(resolve(url).func, cost_chat)

    def test_UserSearch(self):
        url = reverse('chat:usersearch')
        self.assertEqual(resolve(url).func, UserSearch)

    # def test_Directs(self):
    #     url = reverse('chat:free_chat')
    #     self.assertEqual(resolve(url).func, Directs)

    def test_SendDirect(self):
        url = reverse('chat:send_direct')
        self.assertEqual(resolve(url).func, SendDirect)

    def test_Inbox_cost(self):
        url = reverse('chat:Inbox_cost')
        self.assertEqual(resolve(url).func, Inbox_cost)

    def test_Daliy_Tip(self):
        url = reverse('chat:Daliy_Tip')
        self.assertEqual(resolve(url).func, Daliy_Tip)
