import uuid 
import json
from tqdm import tqdm

def parse_input(ds_item): 
    '''
    Read in the input string of the data dictionary, and parse out 'context', 'question', and 'answer' 
    '''
    
    ii = ds_item['input']
    item = ii.split('\n\n')
    output = []

    for i in item:
        if "?" not in i:
            context = i
        q_a = i.split("? ")
        
        if i.endswith('?'):
            question = i
            answer = ds_item["label"]

            output_0 = {'context': context, 'input': question, 'answer': answer, 
                        'length': len(answer.split(' ')), "dataset":"ConvFinQA", 
                        'language':"English", 'all_classes':"N/A", '_id':str(uuid.uuid4())}
            output.append(output_0)
        
        if len(q_a) >= 2:
            question = q_a[0]
            answer = q_a[-1]
            output_0 = {'context': context, 'input': question, 'answer': answer, 
                        'length': len(answer.split(' ')), "dataset":"ConvFinQA", 
                        'language':"English", 'all_classes':"N/A", '_id':str(uuid.uuid4())}
            output.append(output_0)

    return output 

def parse_input_all(list_of_dict): 
    '''
    parameters: 
    list_of_dict: list of dictionaries
    '''
    output = []
    for i in list_of_dict : 
        out = parse_input(i)
        output = output+out
    print("The length of the output is: " + str(len(output)))
    return output 

# Function to convert and write to JSONL
def convert_to_jsonl(list_of_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for data_dict in list_of_dict:
            # Parse the string into a Python dictionary
            try:
                json.dump(data_dict, f, ensure_ascii=False)
                f.write('\n')
            except json.JSONDecodeError as e:
                print(f"Error parsing string: {e}")

if __name__ == "__main__":

    from datasets import load_dataset
    ds = load_dataset("AdaptLLM/finance-tasks", "ConvFinQA")
    output_file = './finance_qna.jsonl'
    output = parse_input_all(ds["test"])
    convert_to_jsonl(output, output_file)