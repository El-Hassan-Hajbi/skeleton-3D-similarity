
def create_DAG(segmented_manifolds : list):
        edges = []
        # find the manifold with max saliency 
        salient_manifold = get_max_saliency(segmented_manifolds)
        # add the max saliency manifold to the graph rooted at '#'
        edges.append(("#", salient_manifold.index))
        # levels from 1 ..


class Manifold:
    def __init__(self, index: int, saliency: float, neighbors=[]):
        self.value = saliency
        self.index = index
        self.neighbors = neighbors

    def __eq__(self, other):
        if isinstance(other, Manifold):
            return self.index == other.index
        return NotImplemented

if __name__ == "__main__":
        import numpy as np
        components = [
                Manifold(index= 1, saliency=0.1189, neighbors = [Manifold(index= 5, saliency=0.0142),Manifold(index= 6, saliency=0.0127)]),
                Manifold(index= 2, saliency=0.7391, neighbors= [Manifold(index= 3, saliency=0.0287),Manifold(index= 4, saliency=0.0267),Manifold(index= 5, saliency=0.0142),Manifold(index= 6, saliency=0.0127),Manifold(index= 8, saliency=0.03),Manifold(index= 7, saliency=0.0298)]),
                Manifold(index= 3, saliency=0.0287, neighbors= [Manifold(index= 2, saliency=0.7391)]),
                Manifold(index= 4, saliency=0.0267, neighbors= [Manifold(index= 2, saliency=0.7391)]),
                Manifold(index= 5, saliency=0.0142, neighbors= [Manifold(index= 2, saliency=0.7391), Manifold(index= 1, saliency=0.1189)]),
                Manifold(index= 6, saliency=0.0127, neighbors= [Manifold(index= 2, saliency=0.7391), Manifold(index= 1, saliency=0.1189)]),
                Manifold(index= 8, saliency=0.03, neighbors= [Manifold(index= 2, saliency=0.7391)]),
                Manifold(index= 7, saliency=0.0298, neighbors= [Manifold(index= 2, saliency=0.7391)]),
        ]
        class segmented_skeleton():
            def __init__(self, neighbors, saliency, manifolds) -> None:
                 self.manifolds = manifolds
                 self.saliency = saliency
                 self.neighbors = neighbors
        neighbors = {
                "1" : ["5", "6"],
                "2" : ["3", "4", "5", "6", "7", "8"],
                "3" : ["2"],
                "4" : ["2"],
                "5" : ["2"],
                "6" : ["1"],
                "7" : ["2"],
                "8" : ["2"],
                     }
        saliency = [0.1189, 0.7391, 0.0287, 0.0267, 0.0142, 0.0127, 0.03, 0.0298] # ordered by manifold index from 1 to 8 in the example
        manifolds = [] # list of list containing voxels described by each manifold
        
        
        segmented_ske = segmented_skeleton(neighbors, saliency, manifolds)
        edges = []
        # get manifold index with max saliency 
        index_max = np.argmax(segmented_ske.saliency) + 1
        edges.append(("#", str(index_max)))
        visited=[str(index_max)]
        # call a recursive function on that manifold
        def recursive_(index):
             # create edge between manifold and all its neighbors 
            for neighb_idx in segmented_ske.neighbors[index]:
                if neighb_idx not in visited:
                    visited.append(neighb_idx)
                    edges.append((index, neighb_idx))
                    recursive_(neighb_idx)
        recursive_(str(index_max))
        print(edges)

