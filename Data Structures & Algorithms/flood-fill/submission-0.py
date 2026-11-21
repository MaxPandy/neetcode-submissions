class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color=image[sr][sc]
        if start_color==color:
            return image
        stack=[(sr,sc)]
        image[sr][sc]=color
        while stack:
            vertex=stack.pop()
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0<=vertex[0]+i<=(len(image)-1) and 0<=vertex[1]+j<=(len(image[0])-1) and image[vertex[0]+i][vertex[1]+j]==start_color:
                    stack.append((vertex[0]+i,vertex[1]+j))
                    image[vertex[0]+i][vertex[1]+j]=color
        return image
