#!/usr/bin/env python3
"""
Script to map wav filenames to models and calculate average MOS scores.
"""

import csv
from collections import defaultdict
from pathlib import Path


def load_mapping(mapping_file):
    """
    Load the mapping from wav filename (UUID) to model name.
    Returns a dictionary: {uuid: model_name}
    """
    mapping = {}
    with open(mapping_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Format: "sentence_id/model_name  uuid"
            parts = line.split()
            if len(parts) >= 2:
                model_path = parts[0]  # e.g., "1/habibi"
                uuid = parts[1]  # e.g., "9e7a2b3c-4d5e-4f6a-8b9c-0d1e2f3a4b5c"
                
                # Extract model name from path
                model_name = model_path.split('/')[-1]
                mapping[uuid] = model_name
    
    return mapping


def calculate_model_averages(csv_file, mapping):
    """
    Calculate average naturalness and clarity scores for each model.
    """
    # Store all scores for each model
    model_scores = defaultdict(lambda: {'naturalness': [], 'clarity': []})
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            wav_filename = row['wav_filename']
            
            # Extract UUID from wav filename (remove .wav extension)
            uuid = wav_filename.replace('.wav', '')
            
            # Get model name from mapping
            if uuid in mapping:
                model_name = mapping[uuid]
                
                # Parse scores
                try:
                    naturalness = float(row['naturalness'])
                    clarity = float(row['clarity'])
                    
                    model_scores[model_name]['naturalness'].append(naturalness)
                    model_scores[model_name]['clarity'].append(clarity)
                except ValueError:
                    print(f"Warning: Could not parse scores for {wav_filename}")
            else:
                print(f"Warning: No mapping found for {uuid}")
    
    # Calculate averages
    results = {}
    for model_name, scores in model_scores.items():
        naturalness_avg = sum(scores['naturalness']) / len(scores['naturalness']) if scores['naturalness'] else 0
        clarity_avg = sum(scores['clarity']) / len(scores['clarity']) if scores['clarity'] else 0
        
        results[model_name] = {
            'naturalness_avg': naturalness_avg,
            'clarity_avg': clarity_avg,
            'num_samples': len(scores['naturalness'])
        }
    
    return results


def main():
    # File paths
    csv_file = 'results/master_mos_results.csv'
    mapping_file = 'mapping.txt'
    
    print("Loading mapping file...")
    mapping = load_mapping(mapping_file)
    print(f"Loaded {len(mapping)} mappings")
    
    print("\nCalculating average scores...")
    results = calculate_model_averages(csv_file, mapping)
    
    print("\n" + "="*70)
    print("AVERAGE MOS SCORES BY MODEL")
    print("="*70)
    print(f"{'Model':<15} {'Naturalness':<15} {'Clarity':<15} {'# Samples':<10}")
    print("-"*70)
    
    # Sort by model name for consistent output
    for model_name in sorted(results.keys()):
        stats = results[model_name]
        print(f"{model_name:<15} {stats['naturalness_avg']:<15.3f} {stats['clarity_avg']:<15.3f} {stats['num_samples']:<10}")
    
    print("="*70)
    
    # Save results to CSV
    output_file = 'results/model_averages.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['model', 'naturalness_avg', 'clarity_avg', 'num_samples'])
        
        for model_name in sorted(results.keys()):
            stats = results[model_name]
            writer.writerow([
                model_name,
                f"{stats['naturalness_avg']:.3f}",
                f"{stats['clarity_avg']:.3f}",
                stats['num_samples']
            ])
    
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
