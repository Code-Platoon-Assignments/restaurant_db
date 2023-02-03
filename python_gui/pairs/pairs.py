import psycopg2
# from ...slack_bot.slack_bot import slack_bot as Slack


class Pairs:
    def __init__(self):
        self.include_list = self.load_student_names_from_file()
        self.do_not_include_list = []
        self.pairs = []
        self.generated_pairs_text = '' 

    def load_student_names_from_file(self):
        list = []
        with open('student_list.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                list.append(line)
        return list

    def generate_pairs(self, list):
        """
          > format `list` into string
          > update `pairs` list
          > return formatted string
        """
        pair_count = 0
        list_iterator = iter(list)
        text = 'Here are the pairs for this week\n'
        
        for name in list_iterator:
            pair_count+=1
 
            text += str(pair_count) + '. ' 
            text += f'{name} ---- '
            second_name = next(list_iterator) 
            text += second_name 
            if (pair_count == len(list)//2) and (len(list) % 2 == 1):
                text  += ' ---- ' + next(list_iterator) 

            text +=  '\n'
            self.generated_pairs_text = text
            self.pairs.append((name, second_name))
        print(self.generated_pairs_text)
        return text

    def send_pairs_to_slack(self):
        blocks = []
        blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": self.generated_pairs_text
                }
            })

        # Slack.send_message('#pairs', 'Here are the pairs for this week')

        # Slack.send_message(channel='#sierra', message ='', blocks=blocks)
        

    def pairs_to_text(self):
        pass



# pairs_interface.generate_pairs(['a','b','c','d', 'e'])
