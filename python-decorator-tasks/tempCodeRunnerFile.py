    def helper(*args, **kwrd):
        helper.calls += 1
        print(helper.calls)
        return func(*args, **kwrd)