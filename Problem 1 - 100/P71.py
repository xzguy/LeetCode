def simplifyPath(path):
    """
    : type path: str
    : rtype: str
    """
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p and p != '.':
            stack.append(p)
    return "/" + "/".join(stack)

input = "/a/./b/../../c/"
print(simplifyPath(input))