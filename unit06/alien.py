
def main():
    alien_0 = {'color':'green', 'points':5}
    print(alien_0['color'])
    print(alien_0['points'])
    print(alien_0.keys())
    print(alien_0.values())
    print(alien_0.items())
    print("="*10)
    for key, _ in alien_0.items():
        print(alien_0[key])
    
    new_points = alien_0['points']
    print(f"You just earned {new_points} points!")

    print("="*10)
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

def create_alien():
    aliens = []
    colors = ['green', 'yellow', 'red', 'blue']
    speeds = ['slow', 'medium', 'fast']
    
    for alien_number in range(10):
        # Using % ensures the index wraps back to 0 when it hits the end
        new_alien = {
            'color': colors[alien_number % len(colors)], 
            'points': 5, 
            'speed': speeds[alien_number % len(speeds)]
        }
        aliens.append(new_alien)
    
    return aliens

def change_alien(aliens):
    for alien in aliens:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15


if __name__ == '__main__':
    aliens  = create_alien()
    for alien in aliens:
        print(alien)
    change_alien(aliens)
    print("="*10)
    for alien in aliens:
        print(alien)
