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

if __name__ == "__main__":
    test_domain_distribution()

