import os

def audit_system():
    print("=== Basic System Audit Tool ===")
    print("\nCurrent Working Directory:", os.getcwd())

    print("\nFiles in Current Directory:")
    for f in os.listdir("."):
        print("-", f)

    print("\nEnvironment Check:")
    print("Operating System:", os.name)

    suspicious=[]
    for f in os.listdir("."):
        if f.endswith(".exe") or f.endswith(".bat"):
            suspicious.append(f)

    print("\nAudit Report")
    if suspicious:
        print("Potential executable files found:")
        for s in suspicious:
            print("-",s)
    else:
        print("No suspicious executable files found.")

if __name__=="__main__":
    audit_system()
