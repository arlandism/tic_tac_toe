import unittest
import json
import json_transmitter
import mock
import socket
from network_io_test_utils import MockSocket

EOF = "\r\n"

class JsonTransmitterTests(unittest.TestCase):

    def setUp(self):
        self.mock = MockSocket()
        self.transmitter = json_transmitter.JsonTransmitter(self.mock)

    def last_sent_arg(self):
        return self.mock.send_args.pop()

    def test_it_receives_its_socket(self):
        self.assertEqual(self.mock,self.transmitter.socket)

    def test_it_jsonifies_load_before_sending(self):
        message = "some stuff"
        jsonified = json.dumps(message)
        self.transmitter.send(message)
        self.assertTrue(self.mock.send_called)
        self.assertEqual(jsonified + EOF,self.last_sent_arg())

    def test_it_jsonifies_nums_before_sending(self):
        num = 3
        jsonified = json.dumps(num)
        self.transmitter.send(num)
        self.assertEqual(jsonified + EOF,self.last_sent_arg())

    def test_it_decodes_json_upon_receipt(self):
        decoded = "message"
        jsonified = json.dumps("message")
        self.mock.add_to_receive_stack(jsonified)
        self.assertEqual(decoded,self.transmitter.receive())

    def test_it_decodes_json_hashes_upon_receipt(self):
        decoded = {1:u'x'}
        jsonified = json.dumps(decoded)
        self.mock.add_to_receive_stack(jsonified)
        self.assertEqual(decoded,self.transmitter.receive())

    def test_it_sends_shutdown_message(self):
        self.transmitter.send("foobar")
        self.assertTrue(self.mock.shutdown_called_with(socket.SHUT_WR))

class HashTransformerTests(unittest.TestCase):

    def setUp(self):
        self.transformer = json_transmitter.HashTransformer

    def assertTransformerWorks(self,dictionary,expected):
        self.assertEqual(expected,self.transformer.try_dict_key_conversion(dictionary))

    def test_it_turns_hash_str_keys_to_ints(self):
        self.assertTransformerWorks( {"1":"x"}, {1:"x"} )

    def test_it_works_for_unicode(self):
        self.assertTransformerWorks( {u"1":u"x"}, {1:"x"} )

    def test_it_knows_how_to_work_with_non_ints(self):
        self.assertTransformerWorks( {"x":"o"}, {"x":"o"} ) 

    def test_on_empty_hashes(self):
        self.assertTransformerWorks( {}, {} )

    def test_it_knows_leaves(self):
        moves = {5:"o", 6:"x"}
        self.assertTrue(self.transformer.is_terminal(moves,5))

    def test_it_know_branches(self):
        hash_ception = {"board": {1:"x", 3:"o"}}
        self.assertFalse(self.transformer.is_terminal(hash_ception,"board"))

    def test_it_converts_nested_hashes(self):
        hash_ception = {"1": {"3":"x", "5":"o"}}
        actual = self.transformer.try_dict_key_conversion(hash_ception)
        self.assertEqual( {1:{3:"x",5:"o"}}, actual)

class JsonTransmitterAndHashTransformerIntegrationTests(unittest.TestCase):
      
    def test_some_json_encoded_stuff_goes_in_and_useful_stuff_comes_out(self):
        mock = MockSocket()
        transmitter = json_transmitter.JsonTransmitter(mock)
        useful = {
            "token_one":"x",
            "token_two":"o",
            "player_one":"human",
            "player_two":"computer",
            "board_size": 4,
            "difficulty":"impossible",
            "board" : {4:"x", 7:"o"}
          }
        useless = json.dumps(useful)
        mock.add_to_receive_stack(useless)
        self.assertEqual(useful,transmitter.receive())
