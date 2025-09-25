"""
Autonomous Delivery Agent (Single File Version, pygame)

- Mouse-controlled menu to choose map
- Algorithm is fixed (A* by default)
- Press ESC during simulation to return to menu
"""

import sys, time, math, random, heapq
import pygame
from collections import deque
from dataclasses import dataclass

# ----------------------------
# MAP DEFINITIONS (inline)
# ----------------------------
MAPS = {
    "Small": [
        ["S","1","1","1","1"],
        ["1","#","#","1","G"],
        ["1","1","1","1","1"],
    ],
    "Medium": [
        ["S","1","1","1","1","1"],
        ["1","1","#","2","2","1"],
        ["1","1","1","3","#","1"],
        ["1","#","1","1","1","G"],
    ],
    "Large": [
        ["S","1","1","2","2","1","1","1","1"],
        ["1","2","3","3","2","1","1","#","1"],
        ["1","1","1","1","1","2","3","1","1"],
        ["1","#","#","1","1","1","2","1","G"],
        ["1","1","1","1","2","2","1","1","1"],
    ],
    "Dynamic": [
        ["S","1","1","1","1","1"],
        ["1","1","1","1","1","1"],
        ["1","1","1","1","1","1"],
        ["1","1","1","1","1","G"],
    ],
}

# For dynamic map, define moving obstacle
DYNAMIC_OBST = [((1,2),(2,2),(3,2),(2,2))]  # moves back and forth

# ----------------------------
# ENVIRONMENT
# ----------------------------
@dataclass
class MovingObstacle:
    path: list
    period: int
    start_time: int = 0
    def position_at(self, t: int):
        if not self.path: return None
        idx = ((t - self.start_time) // self.period) % len(self.path)
        return self.path[idx]

class GridEnvironment:
    def __init__(self, grid, start, goal, moving_obstacles=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = start
        self.goal = goal
        self.moving_obstacles = moving_obstacles or []

    @classmethod
    def from_tokens(cls, tokens, dynamic=False):
        grid = []
        start = goal = None
        for r, row in enumerate(tokens):
            new_row = []
            for c, tok in enumerate(row):
                if tok == "#":
                    new_row.append(None)
                elif tok == "S":
                    start = (r,c); new_row.append(1)
                elif tok == "G":
                    goal = (r,c); new_row.append(1)
                else:
                    new_row.append(int(tok))
            grid.append(new_row)
        moving = []
        if dynamic:
            for path in DYNAMIC_OBST:
                moving.append(MovingObstacle(list(path), period=1))
        return cls(grid,start,goal,moving)

    def cost(self, pos):
        r,c = pos
        return self.grid[r][c] if self.grid[r][c] is not None else float("inf")

    def neighbors(self,pos):
        r,c=pos
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<self.rows and 0<=nc<self.cols and self.grid[nr][nc] is not None:
                yield (nr,nc)

    def moving_obstacle_positions(self,t:int):
        return {mo.position_at(t) for mo in self.moving_obstacles if mo.position_at(t) is not None}

    def is_occupied(self,pos,t:int):
        r,c=pos
        if not (0<=r<self.rows and 0<=c<self.cols): return True
        if self.grid[r][c] is None: return True
        if pos in self.moving_obstacle_positions(t): return True
        return False

# ----------------------------
# SEARCH ALGORITHMS
# ----------------------------
def reconstruct_path(came_from, start, goal):
    path=[];cur=goal
    while cur!=start:
        path.append(cur);cur=came_from[cur]
    path.append(start);path.reverse();return path

def bfs(env,start,goal,**_):
    frontier=deque([start]);came={start:None}
    while frontier:
        cur=frontier.popleft()
        if cur==goal: return reconstruct_path(came,start,goal),0
        for nb in env.neighbors(cur):
            if nb not in came:
                came[nb]=cur;frontier.append(nb)
    return None,0

def uniform_cost_search(env,start,goal,**_):
    pq=[(0,start)];came={};cost={start:0}
    while pq:
        cur_cost,cur=heapq.heappop(pq)
        if cur==goal: return reconstruct_path(came,start,goal),0
        for nb in env.neighbors(cur):
            new_cost=cur_cost+env.cost(nb)
            if nb not in cost or new_cost<cost[nb]:
                cost[nb]=new_cost;came[nb]=cur
                heapq.heappush(pq,(new_cost,nb))
    return None,0

def manhattan(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

def a_star_search(env,start,goal,**_):
    pq=[(manhattan(start,goal),start)]
    g={start:0};came={};visited=set()
    while pq:
        _,cur=heapq.heappop(pq)
        if cur in visited: continue
        visited.add(cur)
        if cur==goal: return reconstruct_path(came,start,goal),0
        for nb in env.neighbors(cur):
            tg=g[cur]+env.cost(nb)
            if nb not in g or tg<g[nb]:
                g[nb]=tg;came[nb]=cur
                heapq.heappush(pq,(tg+manhattan(nb,goal),nb))
    return None,0

ALGOS = {
    "A*": a_star_search,  # Fixed algorithm
}

# ----------------------------
# AGENT + VISUALIZATION
# ----------------------------
CELL=36
class DeliveryAgent:
    def __init__(self,env,planner,visualize=True):
        self.env=env;self.planner=planner;self.visualize=visualize
        self.time_step=0
        if visualize:
            pygame.init()
            w,h=env.cols*CELL,env.rows*CELL+40
            self.screen=pygame.display.set_mode((w,h))
            pygame.display.set_caption("Autonomous Delivery Agent")
            self.clock=pygame.time.Clock()
            self.font=pygame.font.SysFont("Arial",16)
            self.alpha=0
    def draw(self,path=None,pos=None):
        self.screen.fill((240,240,245))
        for r in range(self.env.rows):
            for c in range(self.env.cols):
                rect=pygame.Rect(c*CELL,r*CELL,CELL,CELL)
                v=self.env.grid[r][c]
                color=(40,40,40) if v is None else (max(80,255-(v-1)*18),)*3
                pygame.draw.rect(self.screen,color,rect)
                pygame.draw.rect(self.screen,(200,200,200),rect,1)
        if path:
            for i,(rr,cc) in enumerate(path):
                surf=pygame.Surface((CELL-6,CELL-6),pygame.SRCALPHA)
                surf.fill((50,150,50,180))
                self.screen.blit(surf,(cc*CELL+3,rr*CELL+3))
        for mo in self.env.moving_obstacles:
            p=mo.position_at(self.time_step)
            if p: rr,cc=p;pygame.draw.rect(self.screen,(200,50,50),
                     pygame.Rect(cc*CELL+4,rr*CELL+4,CELL-8,CELL-8))
        sr,sc=self.env.start;gr,gc=self.env.goal
        pygame.draw.rect(self.screen,(30,120,220),pygame.Rect(sc*CELL+6,sr*CELL+6,CELL-12,CELL-12))
        pygame.draw.rect(self.screen,(230,180,40),pygame.Rect(gc*CELL+6,gr*CELL+6,CELL-12,CELL-12))
        if pos:
            rr,cc=pos;cx,cy=cc*CELL+CELL//2,rr*CELL+CELL//2
            self.alpha+=0.08;pulse=6+int(4*math.sin(self.alpha))
            pygame.draw.circle(self.screen,(10,90,40),(cx,cy),CELL//3+pulse)
        hud=f"ESC=Menu  t={self.time_step}"
        self.screen.blit(self.font.render(hud,True,(20,20,20)),(10,self.env.rows*CELL+10))
        pygame.display.flip()
    def run(self):
        path,_=self.planner(self.env,self.env.start,self.env.goal)
        if not path: return "menu"
        idx=0;pos=path[idx]
        while pos!=self.env.goal:
            for event in pygame.event.get():
                if event.type==pygame.QUIT: pygame.quit();sys.exit()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                    return "menu"
            if self.visualize:
                self.draw(path,pos);self.clock.tick(8)
            self.time_step+=1
            nxt=path[min(idx+1,len(path)-1)]
            if self.env.is_occupied(nxt,self.time_step):
                path,_=a_star_search(self.env,pos,self.env.goal)
                idx=0;continue
            idx=min(idx+1,len(path)-1);pos=path[idx]
        if self.visualize: self.draw(path,pos);time.sleep(1)
        return "done"

# ----------------------------
# MENU SCREEN
# ----------------------------
def menu_screen():
    pygame.init()
    screen=pygame.display.set_mode((600,400))
    pygame.display.set_caption("Menu - Autonomous Agent")
    clock=pygame.time.Clock()
    font=pygame.font.SysFont("Arial",28)
    map_keys=list(MAPS.keys())
    buttons = []
    # Precompute button rects
    for i, m in enumerate(map_keys):
        rect = pygame.Rect(200, 100 + i*50, 200, 40)
        buttons.append((m, rect))
    while True:
        screen.fill((245,245,250))
        screen.blit(font.render("Choose Map", True, (30,30,30)), (200,30))
        for m, rect in buttons:
            pygame.draw.rect(screen, (0,150,0), rect)
            screen.blit(font.render(m, True, (255,255,255)), (rect.x+10, rect.y+5))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit();sys.exit()
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                mx,my=e.pos
                for m, rect in buttons:
                    if rect.collidepoint(mx,my):
                        return m, "A*"  # Always use A* algorithm
        clock.tick(30)

# ----------------------------
# MAIN
# ----------------------------
def main():
    while True:
        m,a=menu_screen()
        env=GridEnvironment.from_tokens(MAPS[m], dynamic=(m=="Dynamic"))
        agent=DeliveryAgent(env, ALGOS[a], visualize=True)
        if agent.run()!="menu": break

if __name__=="__main__":
    main()
