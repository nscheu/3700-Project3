#!/usr/bin/python -u

class Buffer:

    def __init__(self):
        self.size = 1
        self.packets = []

    def add(self, packet):
        self.packets.append(packet)

    def get_top(self):
        """
        Gets the first packet from the buffer
        :return:
        """
        if len(self.packets) > 0:
            return self.packets[0]
        else:
            return False

    def remove_top(self):
        """
        Removes the first packet from the buffer
        :return:
        """
        if len(self.packets):
            self.packets.pop(0)

    def free_slots(self):
        """
        Checks how many free slots are in the buffer
        :return: Boolean - True if there are open slots, else False
        """
        return self.size - len(self.packets) > 0

    def sequence_in_buffer(self, sequence_num):
        result = False
        for packet in self.packets:
            if packet['sequence'] == sequence_num:
                return True
        return result

    def insert_packet(self, packet):
        if not len(self.packets):
            self.add(packet)
            return True

        else:
            i = 0
            for curr_pack in self.packets:
                if curr_pack['sequence'] > packet['sequence']:
                    self.packets = self.packets[:i] + [packet] + self.packets[i:]
                    return True
                i += 1
            return False

    def insert_ack_packet(self, packet):
        if not len(self.packets):
            self.add(packet)
            return True

        else:
            i = 0
            for curr_pack in self.packets:
                if curr_pack['ack'] > packet['ack']:
                    self.packets = self.packets[:i] + [packet] + self.packets[i:]
                    return True
                i += 1
            return False

