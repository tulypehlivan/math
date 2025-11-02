class AdaptiveEngine:
    """another difficulty problems."""
    
    def __init__(self):
        self.MAX_STREAK = 3 # difficulty numbers
        self.MAX_LEVEL = 2  # Hard (2)
        self.MIN_LEVEL = 0  # Easy (0)
        
    def determine_next_difficulty(self, tracker, current_difficulty, time_taken, time_threshold):
        """Tracker data used for difficulty."""
        
        # 1. numbers (Streak) 
        streak = 0
        for entry in reversed(tracker.log):
            if entry['correct'] and entry['difficulty'] == current_difficulty:
                streak += 1
            else:
                break
        
        # security control
        if not tracker.log:
            return current_difficulty

        last_correct = tracker.log[-1]['correct']
        
        # if result is msitake you dont do it difficulty
        if not last_correct:
            return max(self.MIN_LEVEL, current_difficulty - 1)
        
        # prosfessinonally(Streak) ve  (Time) add difficulty
        if streak >= self.MAX_STREAK and time_taken <= time_threshold:
            return min(self.MAX_LEVEL, current_difficulty + 1)
        
        # prosfessionally slow  - the same level
        elif streak >= self.MAX_STREAK and time_taken > time_threshold:
            return current_difficulty
        
        # continue series (Streak < 3) - the same level
        else: 
            return current_difficulty