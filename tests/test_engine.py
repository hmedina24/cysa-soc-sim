#test_engine.py

from src.engine import SOCEngine

def test_domain_distribution():
    engine = SOCEngine()
    stats = {domain: 0 for domain in engine.domains.keys()}
    iterations = 1000

    print(f"--- Running {iterations} simulations ---")

    for _ in range(iterations):
        selected = engine.get_next_mission()
        stats[selected] += 1
    
    # Check if Security Operations is roughlt 33% (allowing a 5% margin of error)
    sec_ops_percent = (stats["Security Operations"] / iterations) * 100
    assert 28 <= sec_ops_percent <= 38

    print(f"\nSec Ops was {sec_ops_percent}%")

    print("\nResults:")
    for domain, count in stats.items():
        percentage = (count / iterations) * 100
        expected = engine.domains[domain] * 100
        print(f"{domain}: {percentage:.1f}% (Expected: {expected}%)")

def test_calculate_reward():
    engine = SOCEngine()

    assert engine.user_xp == 0

    # Test Level 1 Correct 
    gain = engine.calculate_reward(is_correct=True, difficulty=1)
    assert gain == 10 
    assert engine.user_xp == 10

    # Test Level 2 Correct (Accumulation)
    gain2 = engine.calculate_reward(is_correct=True, difficulty=2)
    assert gain2 == 25
    assert engine.user_xp == 35

    # Test Level 3 Incorrect 
    gain3 = engine.calculate_reward(is_correct=False, difficulty=3)
    assert gain3 == 0
    assert engine.user_xp == 35

if __name__ == "__main__":
    test_domain_distribution()
    test_calculate_reward()

