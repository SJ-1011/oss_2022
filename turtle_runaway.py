# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, runner2, chaser, catch_radius=20):
        self.canvas = canvas
        self.runner = runner
        self.runner2 = runner2
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.runner2.shape('turtle')
        self.runner2.color('orange')
        self.runner2.penup()
        
        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        self.drawer2 = turtle.RawTurtle(canvas)
        self.drawer2.hideturtle()
        self.drawer2.penup()

        self.drawer3 = turtle.RawTurtle(canvas)
        self.drawer3.hideturtle()
        self.drawer3.penup()


    def is_catched(self):
        p = self.runner.pos()
        r = self.runner2.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        dx2, dy2 = r[0] - q[0], r[1] - q[1]
        if dx**2 + dy**2 < self.catch_radius2:
            return True
        elif dx2**2 + dy2**2 < self.catch_radius2:
            return True
        else:
            return False

    def start(self, init_dist=400, ai_timer_msec=100):
        self.score = 0
        self.start_time = time.time()
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.runner2.setpos((-init_dist / 2, 0))
        self.runner2.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.runner2.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())
        # TODO: You can do something here.
        is_catched = self.is_catched()
        
        if is_catched == True:
            self.score += 1
        self.now_time = time.time() - self.start_time
            
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(f'Is catched? {is_catched}')

        self.drawer2.undo()
        self.drawer2.penup()
        self.drawer2.setpos(-300, 280)
        self.drawer2.write(f'time: {self.now_time:.1f}s')

        self.drawer3.undo()
        self.drawer3.penup()
        self.drawer3.setpos(-300, 260)
        self.drawer3.write(f'your score: {self.score}')                 

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = RandomMover(canvas)
    runner2 = RandomMover(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, runner2, chaser)
    game.start()
    canvas.mainloop()
