from collections import defaultdict

# Danh sách vận động viên
info = [{'name':'L.Marchand', 'nation': 'France', 'programme':'Swimming', 'gold': 4, 'silver':0, 'bronze':1},
       {'name':'T. Huske', 'nation': 'US', 'programme':'Swimming', 'gold': 3, 'silver':2, 'bronze':0},
       {'name':'M. OCallaghan', 'nation': 'Australia', 'programme':'Swimming', 'gold': 3, 'silver':1, 'bronze':1},
       {'name':'S.Biles', 'nation': 'Canada', 'programme':'Artistic gymnastics', 'gold': 3, 'silver':1, 'bronze':0},
       {'name':'M.McIntosh', 'nation': 'France', 'programme':'Swimming', 'gold': 3, 'silver':1, 'bronze':0},
       {'name':'S.Oka', 'nation': 'Japan', 'programme':'Artistic gymnastics', 'gold': 3, 'silver':0, 'bronze':1},
       {'name':'G.Thomas', 'nation': 'US', 'programme':'Athletics', 'gold': 3, 'silver':0, 'bronze':0},
       {'name':'H.Lavreysen', 'nation': 'Netherlands', 'programme':'Track cycling', 'gold': 3, 'silver':0, 'bronze':0},
       {'name':'W.J.Kim', 'nation': 'South Korea', 'programme':'Archery', 'gold': 3, 'silver':0, 'bronze':0},
       {'name':'S.H.Lim', 'nation': 'South Korea', 'programme':'Archery', 'gold': 3, 'silver':0, 'bronze':0}]

# 1. In thông tin ra màn hình dưới dạng bảng đơn giản
print("Danh sách vận động viên:")
print(f"{'Name':<15} {'Nation':<12} {'Programme':<20} {'Gold':<5} {'Silver':<6} {'Bronze':<6}")
print("-" * 64)
for athlete in info:
    print(f"{athlete['name']:<15} {athlete['nation']:<12} {athlete['programme']:<20} {athlete['gold']:<5} {athlete['silver']:<6} {athlete['bronze']:<6}")
print("\n")

# 2. Tìm và in thông tin vận động viên giàu thành tích nhất
info_sorted = sorted(info, key=lambda x: (x['gold'], x['silver'], x['bronze']), reverse=True)
best_athlete = info_sorted[0]
print("Vận động viên giàu thành tích nhất:")
print(f"{'Name':<15} {'Nation':<12} {'Programme':<20} {'Gold':<5} {'Silver':<6} {'Bronze':<6}")
print("-" * 64)
print(f"{best_athlete['name']:<15} {best_athlete['nation']:<12} {best_athlete['programme']:<20} {best_athlete['gold']:<5} {best_athlete['silver']:<6} {best_athlete['bronze']:<6}")
print("\n")

# 3. Tìm và in tên quốc gia giàu thành tích nhất
nation_medals = defaultdict(lambda: {'gold': 0, 'silver': 0, 'bronze': 0})

for athlete in info:
    nation = athlete['nation']
    nation_medals[nation]['gold'] += athlete['gold']
    nation_medals[nation]['silver'] += athlete['silver']
    nation_medals[nation]['bronze'] += athlete['bronze']

nation_sorted = sorted(nation_medals.items(), key=lambda x: (x[1]['gold'], x[1]['silver'], x[1]['bronze']), reverse=True)
best_nation = nation_sorted[0]

print("Quốc gia giàu thành tích nhất:")
print(f"{'Nation':<12} {'Gold':<5} {'Silver':<6} {'Bronze':<6}")
print("-" * 30)
print(f"{best_nation[0]:<12} {best_nation[1]['gold']:<5} {best_nation[1]['silver']:<6} {best_nation[1]['bronze']:<6}")
print("\n")

# 4. Sắp xếp list thông tin theo tổng số lượng huy chương đạt được
for athlete in info:
    athlete['total'] = athlete['gold'] + athlete['silver'] + athlete['bronze']

info_sorted_by_total = sorted(info, key=lambda x: x['total'], reverse=True)

print("Danh sách sắp xếp theo tổng số lượng huy chương:")
print(f"{'Name':<15} {'Nation':<12} {'Programme':<20} {'Gold':<5} {'Silver':<6} {'Bronze':<6} {'Total':<6}")
print("-" * 71)
for athlete in info_sorted_by_total:
    print(f"{athlete['name']:<15} {athlete['nation']:<12} {athlete['programme']:<20} {athlete['gold']:<5} {athlete['silver']:<6} {athlete['bronze']:<6} {athlete['total']:<6}")
print("\n")

# 5. Thống kê số lượng huy chương từng loại của từng nội dung thi đấu
programme_medals = defaultdict(lambda: {'gold': 0, 'silver': 0, 'bronze': 0})

for athlete in info:
    programme = athlete['programme']
    programme_medals[programme]['gold'] += athlete['gold']
    programme_medals[programme]['silver'] += athlete['silver']
    programme_medals[programme]['bronze'] += athlete['bronze']

print("Thống kê huy chương theo nội dung thi đấu:")
print(f"{'Programme':<20} {'Gold':<5} {'Silver':<6} {'Bronze':<6}")
print("-" * 42)
for programme, medals in programme_medals.items():
    print(f"{programme:<20} {medals['gold']:<5} {medals['silver']:<6} {medals['bronze']:<6}")
print("\n")

# 6. Thống kê số lượng huy chương từng loại của từng quốc gia
print("Thống kê huy chương theo quốc gia:")
print(f"{'Nation':<12} {'Gold':<5} {'Silver':<6} {'Bronze':<6}")
print("-" * 30)
for nation, medals in nation_medals.items():
    print(f"{nation:<12} {medals['gold']:<5} {medals['silver']:<6} {medals['bronze']:<6}")
