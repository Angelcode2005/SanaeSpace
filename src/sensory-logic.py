def evaluate_spatial_suitability(decibel_level, lux_level):
    """
    This function evaluates if the environment parameters are
    safe for neurodivergent individuals.
    """
    results = {
        "acoustics": "Optimal" if decibel_level < 50 else "High Noise Alert",
        "lighting": "Safe" if 150 <= lux_level <= 300 else "Adjust Lighting"
    }
    return results
