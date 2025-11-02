import time 

class PerformanceTracker:
    """user time and perfomances"""
    
    def __init__(self, initial_difficulty=0):
        self.log = []
        self.difficulty = initial_difficulty # diary retuns
        self.start_time = time.time()
        self.current_puzzle_start_time = None
        
    def start_puzzle_timer(self):
        """every problems start time"""
        self.current_puzzle_start_time = time.time()
        
    def log_performance(self, is_correct, time_threshold):
        """result and scores"""
        
        # security
        if self.current_puzzle_start_time is None:
            time_taken = 0.0
        else:
            time_taken = time.time() - self.current_puzzle_start_time
        
        # Log loss
        self.log.append({
            'correct': is_correct,
            'time': time_taken,
            'difficulty': self.difficulty 
        })
        
        return time_taken
        
    def get_session_summary(self):
        """seasons finished."""
        total_correct = sum(1 for entry in self.log if entry['correct'])
        total_attempts = len(self.log)
        accuracy = (total_correct / total_attempts) if total_attempts > 0 else 0.0

        correct_times = [entry['time'] for entry in self.log if entry['correct']]
        avg_time = sum(correct_times) / len(correct_times) if correct_times else 0.0
        
        return {
            'accuracy': f"{accuracy * 100:.1f}%",
            'avg_time_correct': f"{avg_time:.2f}s",
            'total_puzzles': total_attempts
        }