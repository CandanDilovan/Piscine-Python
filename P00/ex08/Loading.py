def ft_tqdm(lst: range) -> None:
    """A custom progress bar function that simulates the tqdm progress display.

    Parameters:
    -----------
    lst : range
        A range object specifying the sequence of elements to iterate over.

    Functionality:
    --------------
    - Iterates over each element in the provided range.
    - Calculates the progress as a percentage and updates a loading bar that
      represents the progress visually.
    - Prints the loading bar, current percentage, and the current element in
      the range in real time.
    - Pauses between iterations with a custom delay using `ft_sleep`.
    """
    for elem in lst:
        milestone = 0
        percent = (elem / lst.stop) * 100
        if percent == 0 or percent > milestone + 1:
            milestone = percent
            load_bar = int((elem / lst.stop) * 100)
        loading = "|[" + "=" * load_bar + ">" + " " * (100 - load_bar) + "]|"
        print(f" {int(percent)}%", loading, elem, "/", lst.stop, end='\r')
        ft_sleep(1000000)
        yield elem
    elem += 1
    loading = loading[:-3] + "=>]"
    print("100%", loading, elem, "/", lst.stop, end='\r')
    ft_sleep(50000000)
    return


def ft_sleep(sleep):
    """Custom sleep without time library"""
    for _ in range(sleep):
        pass
