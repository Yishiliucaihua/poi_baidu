def write_list_to_txt(data, path, append):
    f_h = None
    if not append:
        try:
            f_h = open(path, "w")
        except Exception as e:
            print(str(e) + ": " + str(len(data)))
            if f_h:
                f_h.close()
        finally:
            if f_h:
                f_h.close()

    f_h = None
    try:
        f_h = open(path, "a")
        for d in data:
            f_h.write(d)
    except Exception as e:
        print(str(e) + ": " + str(len(data)))
        if f_h:
            f_h.close()
    finally:
        if f_h:
            f_h.close()


def write_line_to_txt(data, path, append):
    f_h = None
    if not append:
        try:
            f_h = open(path, "w")
        except Exception as e:
            print(str(e) + ": " + data)
            if f_h:
                f_h.close()
        finally:
            if f_h:
                f_h.close()

    f_h = None
    try:
        f_h = open(path, "a")
        f_h.write(data)
    except Exception as e:
        print(str(e) + ": " + data)
        if f_h:
            f_h.close()
    finally:
        if f_h:
            f_h.close()


def separate_store(li: list):
    ll = len(li)
    ret = ""
    for i in range(0, ll):
        ret = ret + str(li[i])
        if i != ll - 1:
            ret = ret + "|"
    return ret + "\n"
