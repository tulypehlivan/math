# import
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def get_level_name(level_id):
    """difficulty ID's read name"""
    levels = {0: "EASY", 1: "MEDIUM", 2: "HARD"}
    return levels.get(level_id, "UNKNOWN")

def run_session(num_puzzles=10): # seasons 10 problems
    
    # 1. entry: user entry ve difficulty choseed
    user_name = input("Enter your name: ")
    print("\n--- Initial Setup ---")
    print("Choose initial difficulty: (0: Easy, 1: Medium, 2: Hard)")
    
    try:
        initial_level = int(input("Enter level number (0-2): "))
        if not (0 <= initial_level <= 2):
             initial_level = 0
             print("Invalid input, starting at Easy (0).")
    except ValueError:
        initial_level = 0
        print("Invalid input, starting at Easy (0).")

    # started
    generator = PuzzleGenerator()
    tracker = PerformanceTracker(initial_level)
    engine = AdaptiveEngine() 
    current_difficulty = initial_level
    
    print(f"\nWelcome, {user_name}! Starting at {get_level_name(current_difficulty)}.")

    # 2. main probleem circle
    for i in range(1, num_puzzles + 1):
        
        # Tracker' s we known
        tracker.difficulty = current_difficulty 
        
        # Puzzle make it
        puzzle_data = generator.generate(current_difficulty)
        time_th = puzzle_data['time_threshold']
        
        print(f"\n--- Puzzle {i}/{num_puzzles} (Level: {get_level_name(current_difficulty)}) ---")
        print(f"Problem: {puzzle_data['problem']} = ? (Time Limit: {time_th:.1f}s)")
        
        tracker.start_puzzle_timer()
        
        # user entry
        try:
            user_answer = float(input("Your Answer: "))
        except ValueError:
            user_answer = None

        # check it
        is_correct = (user_answer == puzzle_data['answer'])
        
        #performances save
        time_taken = tracker.log_performance(is_correct, time_th)
        
        # feedback
        if is_correct:
            print(f"✅ Correct! Time: {time_taken:.2f}s.")
        else:
            print(f"❌ Incorrect. The answer was {puzzle_data['answer']}.")

        # 3. another diffulty choosedd
        new_difficulty = engine.determine_next_difficulty(
            tracker, 
            current_difficulty, 
            time_taken, 
            time_th
        )
        
        if new_difficulty != current_difficulty:
            print(f"🧠 Adaptation Triggered: Difficulty changing to {get_level_name(new_difficulty)}")
        
        current_difficulty = new_difficulty

    # 4. summary: seasons report
    print("\n" + "="*40)
    print(f"🚀 Session Summary for {user_name}")
    print("="*40)
    summary = tracker.get_session_summary()
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title():<25}: {value}")
    print(f"Final Recommended Level : {get_level_name(current_difficulty)}")
    print("="*40)

if __name__ == "__main__":
    run_session()