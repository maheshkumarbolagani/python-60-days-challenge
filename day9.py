import random
import copy
import math
import numpy as np
import pandas as pd

# Correct name
n = "B Mahesh Kumar"
l = len(n) - n.count(" ")

# Register number
rno = input("Enter Register Number: ")
num = int(rno[-2:])   # 63 → odd → rotation

def gen_data():
    data = []
    for i in range(15):
        d = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(10, 100),
                "pollution": random.randint(20, 300),
                "energy": random.randint(50, 500)
            },
            "history": [random.randint(10, 100) for _ in range(3)]
        }
        data.append(d)
    return data

def make_copies(data):
    assign = data
    shallow = data[:]
    deep = copy.deepcopy(data)
    return assign, shallow, deep

def mutate(data):
    for i in data:
        i["metrics"]["traffic"] += 5
        i["history"].append(random.randint(10, 100))

        t = i["metrics"]["traffic"]
        p = i["metrics"]["pollution"]
        e = i["metrics"]["energy"]

        i["risk"] = round(math.log(t + p + e) + (l % 5), 2)
    return data

def personalize(data):
    if num % 2 == 0:
        data.reverse()
    else:
        data = data[3:] + data[:3]   # rotation for 63
    return data

def to_df(data):
    rows = []
    for i in data:
        rows.append({
            "zone": i["zone"],
            "traffic": i["metrics"]["traffic"],
            "pollution": i["metrics"]["pollution"],
            "energy": i["metrics"]["energy"],
            "risk": i["risk"]
        })
    return pd.DataFrame(rows)

def analyze(df):
    arr = np.array(df[["traffic", "pollution", "energy"]])
    mean = np.mean(arr, axis=0)
    var = np.var(arr, axis=0)

    anomalies = []
    for i in range(len(df)):
        if df["traffic"][i] > mean[0] + np.std(arr[:, 0]):
            anomalies.append(df["zone"][i])

    # Manual correlation
    t = list(df["traffic"])
    p = list(df["pollution"])

    mt = sum(t) / len(t)
    mp = sum(p) / len(p)

    nume = sum((t[i] - mt) * (p[i] - mp) for i in range(len(t)))
    den1 = sum((t[i] - mt) ** 2 for i in range(len(t)))
    den2 = sum((p[i] - mp) ** 2 for i in range(len(t)))

    corr = nume / math.sqrt(den1 * den2)

    return mean, var, anomalies, corr

def patterns(data):
    risks = [i["risk"] for i in data]
    mx = max(risks)
    mn = min(risks)
    stability = round(1 / (np.var(risks) + 1), 2)

    high = [i["zone"] for i in data if i["risk"] > 5]

    cluster = []
    for i in range(len(high) - 1):
        if high[i + 1] == high[i] + 1:
            cluster.append(high[i])

    return (mx, mn, stability), high, cluster

def decision(avg):
    if avg < 4:
        return "System Stable"
    elif avg < 5:
        return "Moderate Risk"
    elif avg < 6:
        return "High Corruption Risk"
    else:
        return "Critical Failure"

# MAIN EXECUTION
original = gen_data()
before = copy.deepcopy(original)

assign, shallow, deep = make_copies(original)

assign = mutate(assign)
assign = personalize(assign)

print("\n---Before---\n", before[:2])
print("\n---After Assignment---\n", assign[:2])

df = to_df(assign)

mean, var, anomalies, corr = analyze(df)
tup, high, cluster = patterns(assign)

avg_risk = sum(df["risk"]) / len(df)
result = decision(avg_risk)

print("\nDataFrame:\n", df.head())
print("\nOriginal vs Deep Same:", before == deep)
print("\nAnomaly Zones:", anomalies)
print("\nRisk Tuple:", tup)
print("\nHigh Risk Zones:", high)
print("Cluster Zones:", cluster)
print("\nDecision:", result)

if l % 2 == 0:
    print("Observation: Shallow copy affected original due to shared nested objects")
else:
    print("Observation: Deep copy maintained separate structure")

print("\nInsight: Shallow copy corrupts nested structures because inner objects are shared.")
