def optimal_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    page_hits = 0

    for i, page in enumerate(pages):
        if page not in frame:
            # Page fault occurs
            page_faults += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                # Find the optimal page to replace
                future_uses = [float('inf')] * frame_size
                for j in range(frame_size):
                    if frame[j] in pages[i+1:]:
                        future_uses[j] = pages[i+1:].index(frame[j]) + i + 1

                page_to_replace = future_uses.index(max(future_uses))
                frame[page_to_replace] = page
        else:
            # Page hit
            page_hits += 1

        print(f"Page: {page} -> Frame: {frame}")

    print(f"\nTotal Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

optimal_page_replacement(pages, frame_size)
