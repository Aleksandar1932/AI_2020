from exercises.informed_search.graph_explorer import pointnum_to_coords, ecd

if __name__ == '__main__':
    print(pointnum_to_coords(10))

    print(ecd(pointnum_to_coords(6), pointnum_to_coords(11)))
