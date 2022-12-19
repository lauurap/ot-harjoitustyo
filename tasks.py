from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py", pty=True)

@task
def build(ctx):
	ctx.run("python3 src/build.py", pty=True)

@task
def test(ctx):
	ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html", pty=True)

@task
def autopep(ctx):
	ctx.run("autopep8 --in-place --recursive src", pty=True)

@task(autopep)
def lint(ctx):
	ctx.run("pylint src", pty=True)