import tornado.ioloop
import tornado.web

class FibonacciGiver(tornado.web.RequestHandler):
    def get(self, n):
        try:
            n = int(n)
            if n < 0:
                self.set_status(400)
                self.write({"error": "n must be a non-negative integer"})
                return

            result = self.calculate_fibonacci(n)
            if result is not None:
                self.write({"n": n, "fibonacci": result})
        except ValueError:
            self.set_status(400)
            self.write({"error": "n must be an integer"})

    def calculate_fibonacci(self, n):
        if n >= 15000:
            self.set_status(400)
            self.write({"error": "n is too big"})
            return None

        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def make_app():
    return tornado.web.Application([
        (r"/fibonacci/([^/]+)", FibonacciGiver),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    print("Server started at http://localhost:8080")
    tornado.ioloop.IOLoop.current().start()