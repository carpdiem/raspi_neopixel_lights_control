import argparse, subprocess, time

if __name__ == "__main__":
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=float, help='color temperature to simulate (K)')
    parser.add_argument('-b', type=float, help='brightness value, range:[0.0, 1.0]')
    args = parser.parse_args()
    pis = ['northwall-bedroom', 'southwall-bedroom']
    cmds = []
    for pi in pis:
        cmds += [['sshpass', '-p', 'raspberry', 'ssh', 'pi@' + pi, 'sudo python ~/raspi_neopixel_lights/python/examples/room_lights.py -t ' + str(args.t) + ' -b ' + str(args.b)]]
    p = [subprocess.Popen(cmd) for cmd in cmds]
    time.sleep(10)
