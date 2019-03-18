# Hackathon - HashCode 2019

import math;

class Slide:
    def __init__(self, horizontal=True, pictures=[]):
        self.h_type = horizontal;
        self.pictures = pictures;
        self.before = None;
        self.after = None;

    def __str__(self):
        if len(self.pictures) == 2:
            return "{} {}".format(self.pictures[0].index, self.pictures[1].index);
        else:
            return str(self.pictures[0].index);

    def get_tag_set(self):
        tags = set();
        for i in self.pictures:
            tags = tags | set(input_object.pictures[i].tags);
        return list(tags);

    def score(self, input_object):
        score = 0;
        curr_tag_set = self.get_tag_set();
        if self.before != None:
            # calculate before slide
            before_ts = self.before.get_tag_set();
            inter = len(list(before_ts & curr_tag_set))
            first = len(list(before_ts)) - inter;
            second = len(list(curr_tag_set)) - inter;
            score = score + min(first, inter, second);
        if self.after != None:
            # calculate after slide
            after_ts = self.after.get_tag_set();
            inter = len(list(after_ts & curr_tag_set))
            first = len(list(after_ts)) - inter;
            second = len(list(curr_tag_set)) - inter;
            score = score + min(first, inter, second);
        return score;

class Picture:
    def __init__(self, horizontal=True, tags=[], index=-1):
        self.h_type = horizontal;
        self.tags = [i for i in tags
        self.index = index;

    def __str__(self):
        result = ""
        if self.h_type:
            result = result + "H "
        else:
            result = result + "V "
        result = result + str(self.tags);
        return result;

class Input:
    def __init__(self, file_name):
        input_file = open(file_name, "r")
        self.n = int(input_file.readline())
        self.pictures = [Picture() for i in range(0, self.n)]; # array of pictures
        self.word_to_index = {}; # tag to array of image index
        self.priority = []; # tags in order
        self.bag = {}; # count to tags
        self.max_slide_score = None;

        for i in range(0, self.n):
            # Create Picture and store type
            elements = input_file.readline().split();
            if elements[0] == 'V':
                self.pictures[i].h_type = False

            # Populate tag
            for tag in elements[2:]:
                self.pictures[i].tags.append(tag);
                if tag not in self.word_to_index:
                    self.word_to_index[tag] = []
                self.word_to_index[tag].append(i);

            # give picture an index
            self.pictures[i].index = i;

        # Create priority
        for k in self.word_to_index.keys():
            count = len(self.word_to_index[k]);
            if count not in self.bag:
                self.bag[count] = set()
            self.bag[count].add(k);
        sorted_keys = sorted(self.bag.keys(), reverse=True);
        for n in sorted_keys:
            self.priority = self.priority + list(self.bag[n]);

        # Calculate max_slide_score
        self.max_slide_score = math.floor(max(self.bag.keys())/2.0)


    def get_tags(self, index):
        return self.pictures[index].tags;

    def print(self):
        for i in self.pictures:
            print(i);

    def print_t_count(self):
        for k in self.word_to_index.keys():
            print("{}\t: {}".format(k, len(self.word_to_index[k])));

    def get_next_prioritized_image(self, max_p, white_list):
        if len(white_list) == self.n:
            return None;

        priorities_to_check = sorted(self.priority.keys(), reverse=True);
        for p in priorities_to_check:
            if p > max_p:
                continue
            potential_tags = self.priority[p]
            for t in potential_tags:
                images = self.word_to_index[t];
                filtered_images = [];
                for x in images:
                    if x in white_list:
                        filtered_images.append(x);
                if len(filtered_images) != 0:
                    return [self.pictures(filtered_images[0]), p];


    def create_slide_show(self):
        image_bag = set([i for i in range(0, self.n)]);
        priority_levels = set(self.bag.keys())
        curr_p = max(priority_levels);
        seed_picture = self.pictures[self.word_to_index[self.priority[curr_p][0]]]
        curr_picture = seed_picture;
        image_bag.remove(curr_picture.index);

        # get a seed image
        # [curr_image, curr_p] = get_next_prioritized_image(curr_p, image_bag);
        [slide, image_bags] = create_slide(curr_image, image_bags)
        populate_seed_slide(slide, image_bags);

        return output_rows;

    def populate_seed_slide(self, curr_slide, image_bags):
        [before_slide, image_bags] = find_next(self, curr_slide, image_bags)
        [after_slide, image_bags] = find_next(self, curr_slide, image_bags)
        slide.before = before_slide;
        slide.after = after_slide;



    # returns:
    # new_slide: Slide()
    # image_bag: set(1, 2, 3, ...)
    def create_slide(self, picture, available_images):
        # create the first slide
        curr_slide = None;
        if picture.h_type:
            curr_slide = Slide(True,[picture])
        else:
            # find the most disjoint picture
            this_tag_set = set(picture.tags);
            best_partner = self.pictures[available_images[0]]
            best_disjoint_tag_count = 0;
            for i in available_images:
                i_tags = set(self.get_tags(i));
                disjoint_tag_count = len(this_tag_set) - len(this_tag_set & i_tags);
                if disjoint_tag_count > best_disjoint_tag_count:
                    best_partner = self.pictures(i);
                    best_disjoint_tag_count = disjoint_tag_count;
            available_images.remove(best_partner);
            curr_slide = Slide(False, [curr_image, best_partner]);
        return [curr_slide, available_images];


#first = Input("a_example.txt");
first = Input("b_lovely_landscapes.txt");
#first = Input("c_memorable_moments.txt");
#first = Input("d_pet_pictures.txt");
#first = Input("e_shiny_selfies.txt");

print(first.bag.keys());
#print(first.create_slide_show());
# space
# space
# space
# space
# space
# space
# space
# space
# space
# space
# space
