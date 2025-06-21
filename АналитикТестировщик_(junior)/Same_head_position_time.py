# Определяем стороны в которые смотрят головы
head1 = ["forward", "back", "left", "right"]
head2 = ["back", "left", "right"]
head3 = ["right", "left", "forward"]

# Продолжительность каждой фазы
dur1, dur2, dur3 = 10, 15, 20
total = 180
# Определение направления каждой головы в минуту t
count = 0
for t in range(total):
    d1 = head1[(t // dur1) % len(head1)]
    d2 = head2[(t // dur2) % len(head2)]
    d3 = head3[(t // dur3) % len(head3)]
    if d1 == d2 == d3:
        count += 1

print("Всего минут, когда все три головы смотрели в одну сторону:", count)