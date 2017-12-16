import graphics as gfx

import common 

import apple as appleFuncs

SPEED = 10

def testForAppleProjectileCollision(projectile, apples):
    for apple in apples[:]:
        appleCenter = apple.getCenter()
        projCenter  = projectile.getCenter()
        if common.distanceBetween(appleCenter, projCenter) < appleFuncs.DIAMETER:
            appleFuncs.removeApple(apples, apple)

def moveProjectile(direction, projectile):
    dx = direction.getX()
    dy = direction.getY()
    #direction.y += 0.05    #Apply gravity
    projectile.move(dx, dy)

def update(projectiles, projectileDirections, apples):
    '''Updates the player's projectiles'''
    removeMe = []
    for i in range(len(projectiles)):
        moveProjectile(projectileDirections[i], projectiles[i])
        testForAppleProjectileCollision(projectiles[i], apples)
        if projectiles[i].getCenter().y - appleFuncs.DIAMETER > common.WINDOW_HEIGHT:
            removeMe.append(i)

    for x in removeMe:
        projectiles[i].undraw()
        projectileDirections.pop(x)
        projectiles.pop(x)

def create(playerPoint, target, window):
    dx, dy = common.getPointDifference(playerPoint, target)
    proj = appleFuncs.makeDefaultApple(playerPoint.getX(), playerPoint.getY(), window)

    dirVector = common.normalise(gfx.Point(dx, dy))
    dx = dirVector.getX() * SPEED
    dy = dirVector.getY() * SPEED
    velocity = gfx.Point(dx, dy)

    return proj, velocity