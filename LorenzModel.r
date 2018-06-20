#Lorenz Model

library(ggplot2)

move <- function(dt) {
    t = seq(0,60,dt)

    x = numeric(length(t))
    y = numeric(length(t))
    z = numeric(length(t))

    # initial conditions
    x[1] = 1

    # constants
    sigma = 10
    b = 8/3
    r = 25

    for (i in seq(length(t)-1)) {
       x[i+1] = x[i] + (sigma*(y[i]-x[i]))*dt
       y[i+1] = y[i] + (-x[i]*z[i] + r*x[i] - y[i])*dt
       z[i+1] = z[i] + (x[i]*y[i] - b*z[i])*dt
    }

    # para sa ggplot2
    df = data.frame(t,x,y,z)

    p = ggplot(df, aes(x)) + geom_point(aes(y=z))

    plot(p)
}

main <- function(){
   TIME_STEP = 0.0001
   move(TIME_STEP)
}

main()
