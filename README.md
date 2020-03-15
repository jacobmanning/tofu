# tofu
tofu is a (light) wrapper around `docker` for building and executing code in a docker container rather than on your machine. The scope of this project is small: it was only written so I could develop on macOS with linux tools.

**Disclaimer:** I wrote this to fit my use cases. No promises that you find this useful at all.

## Requirements
Python 3.6+

## Set up
First, clone this repo in your home directory
```
$ cd ~
$ git clone https://github.com/jacobmanning:tofu
```

Then "install" tofu by creating an alias for it in your `~/.bashrc` (or similar)
```
alias tofu="python3 $HOME/tofu/scripts/impl/tofu.py"
```

## Basic Usage
To use `tofu` for a project, create a `Tofufile` in your project directory. A `Tofufile` is just a Dockerfile. It must have all of the dependencies for your build/execution.

Now, let's have `tofu` build our `Tofufile`. Simply run `tofu build`.

Now that we have built our container, let's start it in the background using `tofu run`.

At this point we've 1) built our tofu docker container and 2) started running it so that we can attach.

Finally, `tofu exec <COMMAND>` to run `<COMMAND>` inside the container!

```
tofu exec ls
```

## Usage
The above probably does not seem useful. But, it can be if we have installed meaningful packages in our tofu container that are not on our host system.

For example, perhaps you've installed bazel in the Tofufile for your build system.

Now, you can do the following:
```
tofu exec bazel build //...
tofu exec bazel test //...
```

This will run bazel inside the tofu container--a command that may not work on your host system!
