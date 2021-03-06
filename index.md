---
title: AliceOS Docs
homepage: true
permalink: /index
---
<style>
    #docs-hero {
        background-image: url('../media/img/hero-doc.png');
        padding-top: 128px;
        padding-bottom: 128px;
    }
</style>
<div class="p-strip--image is-dark" id = "docs-hero">
    <div class="p-content__row shadow">
        <div class="col-8">
            <h1>AliceOS Documentation (master)</h1>
            <p>AliceOS brings new features and experiences to any Ren'Py project. From giving users notifications to its extensibility with Applets, AliceOS makes any visual novel more exciting and enriching for its players and developers.</p>
        </div>
    </div>
</div>
<div class="p-strip">
    <div class="p-content__row">
        <div class="u-equal-height">
            <div class="col-12">
                <h2>Getting started</h2>
                <div>
                    <p>If you want to use AliceOS with any particular version of the Ren'Py SDK, it's best to grab a copy of the source code and compile it manually:</p>
                    <p><pre>
git clone https://github.com/ProjectAliceDev/aliceos.git
                    </pre></p>
                    <p>
                        To add the source code directly to your game, take the contents of the root directory and copy them over to your Ren'Py project's <code>game</code> folder.
                    </p>
                    <p>
                        <div class="p-notification--caution">
                          <p class="p-notification__response">
                            <span class="p-notification__status">Important:</span>Back up your data and settings before performing an upgrade to AliceOS. Some features or settings may be overwritten when <code>git fetch; git pull</code> is run.
                          </p>
                        </div>
                    </p>
                </div>
            </div>
        </div>
        <hr class="is-deep">
        <div class="u-equal-height">
            <div class="col-12">
                <h3>Module System (BETA)</h3>
                <div>
                    <p>Alternatively, developers can make use of the AliceOS Module system. Developers can download the base RPA package for their respective version of Ren'Py (6.99.12.4 or 7+) and continue to build off of this with their own source code. This gives developers and OEMs an easier method to updating the AliceOS core without needing to completely modify the existing installation.</p>
                    <p>This version is still a work-in-progress and may not work as expected.</p>
                    <p><a href = "https://github.com/ProjectAliceDev/aliceos/releases/" class = "p-button--positive p-link--external">Download</a></p>
                </div>
            </div>
        </div>
        <hr class="is-deep">
        <div class="u-equal-height">
            <div class="col-6">
                <h2>Getting support</h2>
                <ul class="p-list">
                    <li class="p-list__item">
                        <a class="p-link--external" href="https://discord.gg/tdvNzjW">Discord</a>
                    </li>
                    <li class="p-list__item">
                        <a class="p-link--external" href="https://reddit.com/r/TheAngelReturns">Reddit</a>
                    </li>
                </ul>
            </div>
            <div class="col-6">
                <h2>Contribute</h2>
                <ul class="p-list">
                    <li class="p-list__item"><a class="p-link--external" href="https://github.com/ProjectAliceDev/aliceos">Push some code</a></li>
                    <li class="p-list__item--deep"><a class="p-link--external" href="https://github.com/ProjectAliceDev/aliceos/issues/new">File an issue</a></li>
                    <li class="p-list__item"><a class="p-link--external" href="https://github.com/ProjectAliceDev/aliceos-docs">Write some docs</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>
