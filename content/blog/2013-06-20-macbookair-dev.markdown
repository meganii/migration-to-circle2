---

title: MacBookAir Mid 2013環境構築
date: 2013-06-20T00:58:00+09:00
category: ['Tech']
tags: ['Mac']
published: true
slug: macbookair-dev
---

MabBookAirの環境設定。
とりあえず、Homebrewとrbenvを入れたときの備忘録。


{{% googleadsense %}}


## Xcodeのインストール
App StoreからXcodeをインストール。


## Homebrewのインストール

```
$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
==> This script will install:
/usr/local/bin/brew
/usr/local/Library/...
/usr/local/share/man/man1/brew.1

Press ENTER to continue or any other key to abort
==> /usr/bin/sudo /bin/mkdir /usr/local

WARNING: Improper use of the sudo command could lead to data loss
or the deletion of important system files. Please double-check your
typing when using sudo. Type "man sudo" for more information.

To proceed, enter your password, or type Ctrl-C to abort.

Password:
==> /usr/bin/sudo /bin/chmod g+rwx /usr/local
==> /usr/bin/sudo /usr/bin/chgrp admin /usr/local
==> Downloading and Installing Homebrew...
remote: Counting objects: 116619, done.
remote: Compressing objects: 100% (55278/55278), done.
remote: Total 116619 (delta 80742), reused 93671 (delta 60389)
Receiving objects: 100% (116619/116619), 18.77 MiB | 95 KiB/s, done.
Resolving deltas: 100% (80742/80742), done.
From https://github.com/mxcl/homebrew
 * [new branch]      master     -> origin/master
HEAD is now at 6ffa175 ccache: added symlinks for more compiler versions
Warning: Install the "Command Line Tools for Xcode": http://connect.apple.com
==> Installation successful!
You should run `brew doctor' *before* you install anything.
Now type: brew help
```

ここで、ちゃんとHomebrewがインストールされているか確認するために、以下のコマンドを叩く。

```
$ brew doctor
Warning: Experimental support for using Xcode without the "Command Line Tools".
You have only installed Xcode. If stuff is not building, try installing the
"Command Line Tools for Xcode" package provided by Apple.

```

すると、Xcodeはインストールしたけど、　Command Line Tools for Xcodeがないと怒られた。


Xcodeを開いて、Xcode > Preferences > Downloads 
のところに、　Command Line Tools という項目があるので、インストール。



<p><a href="http://www.flickr.com/photos/35571855%40N06/9085897322/" title="CommandLineToolsXcode by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm3.staticflickr.com/2857/9085897322_378c2478b7.jpg"  alt="CommandLineToolsXcode" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9085897322/">CommandLineToolsXcode</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>


再び、　brew doctor

```
$ brew doctor
Your system is ready to brew.
```

正常にインストールされているようです。

次に Homebrewを使って環境を整える。

## gitのインストール

```
brew install git
==> Downloading http://git-core.googlecode.com/files/git-1.8.3.1.tar.gz
######################################################################## 100.0%
==> make prefix=/usr/local/Cellar/git/1.8.3.1 CC=cc CFLAGS= LDFLAGS= install
==> make CC=cc CFLAGS= LDFLAGS=
==> make clean
==> make CC=cc CFLAGS= LDFLAGS=
==> Downloading http://git-core.googlecode.com/files/git-manpages-1.8.3.1.tar.gz
######################################################################## 100.0%
==> Downloading http://git-core.googlecode.com/files/git-htmldocs-1.8.3.1.tar.gz
######################################################################## 100.0%
==> Caveats
The OS X keychain credential helper has been installed to:
  /usr/local/bin/git-credential-osxkeychain

The 'contrib' directory has been installed to:
  /usr/local/share/git-core/contrib

Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completion has been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/git/1.8.3.1: 1324 files, 28M, built in 60 seconds
```

## RVMからrbenvへ変更
RVMは、環境を勝手に書き換えることがあるそうなので、rbenvの方がいいという記事も見かけた。
ということで今回は、気持ちの問題で、RVMからrbenvへ乗り換えました(あまり使いこなしていないので、どっちでもいいのだが)。


### Ruby-buildのインストール

```
$ brew install ruby-build
==> Installing ruby-build dependency: autoconf
==> Downloading http://ftpmirror.gnu.org/autoconf/autoconf-2.69.tar.gz
######################################################################## 100.0%
==> ./configure --prefix=/usr/local/Cellar/autoconf/2.69
==> make install
🍺  /usr/local/Cellar/autoconf/2.69: 69 files, 2.0M, built in 16 seconds
==> Installing ruby-build dependency: pkg-config
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/pkg-config-0.28.mountain_lion.bottle.tar.gz
######################################################################## 100.0%
==> Pouring pkg-config-0.28.mountain_lion.bottle.tar.gz
🍺  /usr/local/Cellar/pkg-config/0.28: 10 files, 636K
==> Installing ruby-build
==> Downloading https://github.com/sstephenson/ruby-build/archive/v20130518.tar.gz
######################################################################## 100.0%
==> ./install.sh
🍺  /usr/local/Cellar/ruby-build/20130518: 79 files, 352K, built in 4 seconds
```


### rbenvのインストール

```
$ brew install rbenv
==> Downloading https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz
######################################################################## 100.0%
==> Caveats
To use Homebrew's directories rather than ~/.rbenv add to your profile:
  export RBENV_ROOT=/usr/local/var/rbenv

To enable shims and autocompletion add to your profile:
  if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
==> Summary
🍺  /usr/local/Cellar/rbenv/0.4.0: 31 files, 152K, built in 3 seconds
```

### bash_profileにパスを追加
.bash_profileを作成して、以下の2行を追加。

```
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
```

### ruby 1.9.3をインストール

```
$ rbenv install 1.9.3-p286
Downloading yaml-0.1.4.tar.gz...
-> http://dqw8nmjcqpjn7.cloudfront.net/36c852831d02cf90508c29852361d01b
Installing yaml-0.1.4...
Installed yaml-0.1.4 to /Users/meganii/.rbenv/versions/1.9.3-p286

Downloading ruby-1.9.3-p286.tar.gz...
-> http://dqw8nmjcqpjn7.cloudfront.net/e2469b55c2a3d0d643097d47fe4984bb
Installing ruby-1.9.3-p286...
Installed ruby-1.9.3-p286 to /Users/meganii/.rbenv/versions/1.9.3-p286
```

### OpenSSLをインストール
後々に、このモジュールが必要になる場合があるというので、今のうちにインストール。

```
$ brew install openssl
==> Downloading http://openssl.org/source/openssl-1.0.1e.tar.gz
######################################################################## 100.0%
==> perl ./Configure --prefix=/usr/local/Cellar/openssl/1.0.1e --openssldir=/usr/local/etc/openssl zlib-dynamic shared darwin64-
==> make
==> make test
==> make install MANDIR=/usr/local/Cellar/openssl/1.0.1e/share/man MANSUFFIX=ssl
==> Caveats
To install updated CA certs from Mozilla.org:

    brew install curl-ca-bundle

This formula is keg-only: so it was not symlinked into /usr/local.

Mac OS X already provides this software and installing another version in
parallel can cause all kinds of trouble.

The OpenSSL provided by OS X is too old for some software.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.1e: 429 files, 15M, built in 4.6 minutes
```

### readlineをインストール
readlineもいるんじゃない？っていう記事を見かけたのでついでに入れておく。

```
brew install readline
==> Downloading http://ftpmirror.gnu.org/readline/readline-6.2.tar.gz
######################################################################## 100.0%
==> Patching
patching file callback.c
patching file input.c
patching file patchlevel
patching file support/shobj-conf
patching file vi_mode.c
==> ./configure --prefix=/usr/local/Cellar/readline/6.2.4 --mandir=/usr/local/Cellar/readline/6.2.4/share/man --infodir=/usr/loc
==> make install
==> Caveats
This formula is keg-only: so it was not symlinked into /usr/local.

OS X provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/6.2.4: 31 files, 1.6M, built in 35 seconds
```

### デフォルトで使うRubyのバージョンを指定

```
$ rbenv global 1.9.3-p426
```

```
$ which gem
/Users/meganii/.rbenv/shims/gem
```
gemのPATHもちゃんと変わりました。

## Jekyllの設定

```
$ gem install bundler
```

## Jekyllの設定

```
$ gem install jekyll
Fetching: liquid-2.5.0.gem (100%)
Fetching: fast-stemmer-1.0.2.gem (100%)
Building native extensions.  This coeuld take a while...
Fetching: classifier-1.3.3.gem (100%)
Fetching: directory_watcher-1.4.1.gem (100%)
Fetching: syntax-1.0.0.gem (100%)
Fetching: maruku-0.6.1.gem (100%)
Fetching: kramdown-1.0.2.gem (100%)
Fetching: yajl-ruby-1.1.0.gem (100%)
Building native extensions.  This could take a while...
Fetching: posix-spawn-0.3.6.gem (100%)
Building native extensions.  This could take a while...
Fetching: pygments.rb-0.5.0.gem (100%)
Fetching: highline-1.6.19.gem (100%)
Fetching: commander-4.1.3.gem (100%)
Fetching: safe_yaml-0.7.1.gem (100%)
Fetching: colorator-0.1.gem (100%)
Fetching: jekyll-1.0.3.gem (100%)
Successfully installed liquid-2.5.0
Successfully installed fast-stemmer-1.0.2
Successfully installed classifier-1.3.3
Successfully installed directory_watcher-1.4.1
Successfully installed syntax-1.0.0
Successfully installed maruku-0.6.1
Successfully installed kramdown-1.0.2
Successfully installed yajl-ruby-1.1.0
Successfully installed posix-spawn-0.3.6
Successfully installed pygments.rb-0.5.0
Successfully installed highline-1.6.19
Successfully installed commander-4.1.3
Successfully installed safe_yaml-0.7.1
Successfully installed colorator-0.1
Successfully installed jekyll-1.0.3
15 gems installed
Installing ri documentation for liquid-2.5.0...
Installing ri documentation for fast-stemmer-1.0.2...
Installing ri documentation for classifier-1.3.3...
Installing ri documentation for directory_watcher-1.4.1...
Installing ri documentation for syntax-1.0.0...
Installing ri documentation for maruku-0.6.1...
Couldn't find file to include 'MaRuKu.txt' from lib/maruku.rb
Installing ri documentation for kramdown-1.0.2...
Installing ri documentation for yajl-ruby-1.1.0...
Installing ri documentation for posix-spawn-0.3.6...
Installing ri documentation for pygments.rb-0.5.0...
Installing ri documentation for highline-1.6.19...
Installing ri documentation for commander-4.1.3...
Installing ri documentation for safe_yaml-0.7.1...
Installing ri documentation for colorator-0.1...
Installing ri documentation for jekyll-1.0.3...
Installing RDoc documentation for liquid-2.5.0...
Installing RDoc documentation for fast-stemmer-1.0.2...
Installing RDoc documentation for classifier-1.3.3...
Installing RDoc documentation for directory_watcher-1.4.1...
Installing RDoc documentation for syntax-1.0.0...
Installing RDoc documentation for maruku-0.6.1...
Couldn't find file to include 'MaRuKu.txt' from lib/maruku.rb
Installing RDoc documentation for kramdown-1.0.2...
Installing RDoc documentation for yajl-ruby-1.1.0...
Installing RDoc documentation for posix-spawn-0.3.6...
Installing RDoc documentation for pygments.rb-0.5.0...
Installing RDoc documentation for highline-1.6.19...
Installing RDoc documentation for commander-4.1.3...
Installing RDoc documentation for safe_yaml-0.7.1...
Installing RDoc documentation for colorator-0.1...
Installing RDoc documentation for jekyll-1.0.3...
```
