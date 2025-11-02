import random

# difficulyt
DIFFICULTY_RANGES = {
    0: {'op': ['+'], 'max_val': 10, 'time_th': 5.0},      # Easy: add
    1: {'op': ['+', '-'], 'max_val': 50, 'time_th': 10.0},    # Medium: add and substances
    2: {'op': ['x', '/'], 'max_val': 100, 'time_th': 15.0},   # Hard:divided
}

class PuzzleGenerator:
    """random math problems."""
    
    def generate(self, difficulty_level):
        settings = DIFFICULTY_RANGES[difficulty_level]
        operation = random.choice(settings['op'])
        max_val = settings['max_val']
        
        # correct number
        if operation == '+':
            num1 = random.randint(1, max_val // 2)
            num2 = random.randint(1, max_val - num1)
            correct_answer = num1 + num2
        elif operation == '-':
            num1 = random.randint(1, max_val)
            num2 = random.randint(1, num1)
            correct_answer = num1 - num2
        elif operation == 'x':
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 10)
            correct_answer = num1 * num2
        elif operation == '/':
            # divided
            correct_answer = random.randint(2, 10)
            divisor = random.randint(2, 10)
            num1 = correct_answer * divisor
            num2 = divisor
            
        return {
            'problem': f"{num1} {operation} {num2}",
            'answer': correct_answer,
            'time_threshold': settings['time_th'] # Adaptive Engine for time
        }