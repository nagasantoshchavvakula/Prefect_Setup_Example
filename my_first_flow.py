from prefect import flow, task
import time

@task
def say_hello(name: str) -> str:
    '''
    A simple task that says hello to the given name.
    '''
    print(f"Hello, {name}")
    return f"Hello, {name}"

@task
def process_data(data: str) -> str:
    '''
    A task that simulates processing data.
    '''
    time.sleep(2)  # Simulating a delay
    processed=data.upper()
    print(f"Processed data: {processed}")
    return processed

@flow
def hello_flow(name: str = "World") -> str:
    """
    A simple flow that greets a user and processes some data.
    """
    greeting = say_hello(name)
    result = process_data(greeting)
    return result

if __name__ == "__main__":
    # Run the flow with a sample name
    hello_flow("Prefect")


