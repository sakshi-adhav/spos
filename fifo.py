def fifo_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    page_hits = 0
    page_order = []  # To keep track of the order of pages

    for page in pages:
        if page not in frame:
            # Page fault occurs
            page_faults += 1
            if len(frame) < frame_size:
                frame.append(page)
                page_order.append(page)
            else:
                # Replace the oldest page
                oldest_page = page_order.pop(0)
                frame[frame.index(oldest_page)] = page
                page_order.append(page)
        else:
            # Page hit
            page_hits += 1

        print(f"Page: {page} -> Frame: {frame}")

    print(f"\nTotal Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

fifo_page_replacement(pages, frame_size)
