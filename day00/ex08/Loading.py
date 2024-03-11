# from time import time
import time
import shutil


def format_time(seconds: int):
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    # nombre d'actualisations par seconde :
    nbActualisation = 10

    start = time.time()
    progress_chars = ["▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    rangeLen = len(str(len(lst)))
    lastPrint = time.time()
    for i, item in enumerate(lst, start=1):
        if (time.time() - lastPrint > 1 / nbActualisation
                or i == 1 or i == len(lst)):
            terminalWidth = shutil.get_terminal_size().columns
            ratio = i / len(lst)
            percent = ratio * 100
            iteration = i / (time.time() - start)
            totalWidth = (terminalWidth - 28 - (rangeLen + len(str(i))) -
                          len(str(f"{iteration:.2f}")))
            toFill = (totalWidth * ratio)
            progressChar = toFill - int(toFill)
            if (ratio == 1):
                progressChar = ""
            else:
                progressChar = (progress_chars[int((progressChar -
                                int(progressChar)) * len(progress_chars))])

            iterationFormated = f"{i:.0f}/{len(lst)}"
            infos = f"{percent:3.0f}%"
            timeElapsed = format_time(time.time() - start)
            bar = (f"{'█' * (int(toFill))}"
                   f"{progressChar}"
                   f"{' ' * (totalWidth - int(toFill) - 1)}")

            if i != 1:
                iterationPerSec = f"{iteration:0.2f}"
                timeRemaining = format_time((len(lst) - i) / iteration)
            else:
                iterationPerSec = "1"
                timeRemaining = "00:00"

            lastPrint = time.time()
            print(f"\r{infos}|{bar}| {iterationFormated}"
                  f" [{timeElapsed}<{timeRemaining}, {iterationPerSec}it/s]",
                  end="", flush=True)
        yield item
