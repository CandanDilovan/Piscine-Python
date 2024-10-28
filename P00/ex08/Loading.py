def ft_tqdm(lst: range) -> None:
    for elem in lst:
        percent = (elem / lst.stop) * 100
        if percent == 0 or percent > milestone + 0.25:
            milestone = percent
            loading_bar = int((elem / lst.stop) * 175)
        loading = "[" + "=" * loading_bar + ">" + " " * (175 - loading_bar) + "]"
        print(f" {int(percent)}%", loading, elem, "/", lst.stop, end='\r')
        ft_sleep(1000000)
    elem += 1
    loading = loading[:-3] + "=>]"
    print("100%" ,loading, elem, "/", lst.stop, end='\r')
    ft_sleep(50000000)
    yield lst

def ft_sleep(sleep):
    for _ in range(sleep):
        pass