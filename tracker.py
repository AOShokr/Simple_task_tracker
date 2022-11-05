import csv
import datetime
import sys
from tabulate import tabulate


def main():
    while True:
        
        # instructions for the user
        print("- Write the task you just did, or type 'Display' to view the tasks already on file, or type 'Exit' to exit")
        
        # getting the input from the user
        user_inp = input('Gimme something: ').strip()
        
        # if conditional to determine the user's intention and proceed accordingly
        # in case the user wants to exit
        if user_inp.lower() == 'exit':
            sys.exit()
        
        # in case the user wants to display existing tasks
        elif user_inp.lower() == 'display':
            dics,counts = display()
            if len(dics) == 0:
                print("No Tasks on File")
            else:
                print(tabulate(dics,headers='keys',tablefmt='grid',maxcolwidths=[50,None,None]))
                print("\nSummary By Topic:")
                counts_ordered = sorted(counts.items(),key=lambda x:x[1],reverse=True)
                for k,v in counts_ordered:
                    print(k,v)
        
        # placeholder for clearing mechanism to be implemented
        elif user_inp == "GlUrck":
            with open('list.csv','w') as file:
                ow = csv.DictWriter(file,fieldnames=['action','topic','the_date'])
                ow.writeheader()
        
        # to enter an actual task
        else:
            topic = input('The topic is? ')
            track_this(user_inp.lower(),topic)




# writes down the tast in a .csv file
def track_this(action,topic='General'):
    line = {'action':action.capitalize(),'topic':topic.capitalize(),'the_date':datetime.date.today()}
    with open('list.csv','a',newline = '') as file:
        csv.DictWriter(file,fieldnames=['action','topic','the_date']).writerow(line)

# the function to return the lists of tasks on file
def display():
    dicting = []
    counts = {}
    with open('list.csv','r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            dicting.append({'action':line['action'],'topic':line['topic'],'the_date':line['the_date']})
            if line['topic'] in counts:
                counts[line['topic']] += 1
            else:
                counts[line['topic']] = 1
        return dicting,counts



if __name__ == "__main__":
    main()
