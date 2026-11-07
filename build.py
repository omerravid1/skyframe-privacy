"""Builds the Skyframe pages: one header and footer, each page's body below. Run: python3 build.py"""

EMAIL = "skyframe1992@gmail.com"
UPDATED = "November 7, 2026"

PAGES = [
    ("index.html", "Privacy policy"),
    ("terms.html", "Terms of use"),
    ("delete-account.html", "Delete your account"),
    ("accessibility.html", "Accessibility"),
    ("support.html", "Support"),
]


def page(filename, title, body):
    nav = "\n".join(
        f'        <li><a href="{f}"{" aria-current=\"page\"" if f == filename else ""}>{t}</a></li>'
        for f, t in PAGES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Skyframe — {title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header>
    <p><strong>Skyframe</strong></p>
    <nav aria-label="Skyframe pages">
      <ul>
{nav}
      </ul>
    </nav>
  </header>
  <main id="main">
    <h1>{title}</h1>
    <p class="muted">Last updated {UPDATED}</p>
{body}
  </main>
  <footer>
    <p>Skyframe is a free puzzle game for iPhone, iPad, Android and the web.
      Contact: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </footer>
</body>
</html>
"""


PRIVACY = f"""
    <p>Skyframe is a free falling-block puzzle game. It has no ads, no in-app purchases, no
      analytics and no tracking, and it never sells data. This policy explains the little data the
      game does handle, and your rights over it.</p>

    <h2>Who is responsible</h2>
    <p>Skyframe, an independent game, is the controller of the data described here. Contact:
      <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>Data that stays on your device</h2>
    <p>Your progress (stages unlocked, best scores, My scores), settings (language, look, sound) and
      the name and flag you last used are saved only on your device. They never leave it, and they
      are removed when you uninstall the game or clear the site's data.</p>

    <h2>Data used for the World high-score board</h2>
    <p>Nothing is sent anywhere unless you choose to save a score to the World board, sign in, or
      report a name. Then:</p>
    <table>
      <thead><tr><th scope="col">Data</th><th scope="col">Why</th><th scope="col">Who can see it</th></tr></thead>
      <tbody>
        <tr><td>A player ID: a random ID that Firebase gives your device (a "guest" account) the first time you save a score</td><td>To know which board entry is yours</td><td>Only us and our provider</td></tr>
        <tr><td>The name you type (3–12 characters) and the flag you choose (a country code, or none)</td><td>To show your entry on the board</td><td><strong>Everyone who opens the board</strong></td></tr>
        <tr><td>Your best score, the stage it reached, the incoming threat you played against, and when it was saved</td><td>To rank the board</td><td>Score: everyone. The rest: only us</td></tr>
        <tr><td>If you sign in with Apple (iPhone, iPad) or Google (Android): the account identifier that Apple or Google gives the game, and, for Google, your email address. Skyframe asks Apple for no name and no email.</td><td>To keep your entry when you change phones</td><td>Only us and our provider</td></tr>
        <tr><td>If you report a name: the reported player's ID and name, and the time. Who reported is not stored.</td><td>To review names that may break the rules</td><td>Only us</td></tr>
        <tr><td>Technical data such as your IP address and device type, handled by our provider when the game connects</td><td>Security and abuse prevention</td><td>Only our provider</td></tr>
      </tbody>
    </table>
    <p>The flag starts as the region set on your device (for example, Israel for "Hebrew (Israel)").
      The game never uses your location.</p>

    <h2>Legal basis</h2>
    <p>We process this data to provide the board and the account you asked for (performance of a
      contract, GDPR Art. 6(1)(b)), and to keep the board safe and free of abuse (legitimate
      interests, Art. 6(1)(f)).</p>

    <h2>Who processes the data</h2>
    <p>The board and accounts run on Google Firebase (Cloud Firestore and Firebase Authentication),
      operated by Google as our processor. Board data is stored in the European Union (Firestore
      region "eur3"); Firebase Authentication may process data in the United States. Transfers
      outside the EU rely on Google's certification under the EU–US Data Privacy Framework and the
      European Commission's Standard Contractual Clauses in Google's data processing terms. Apple
      and Google handle sign-in under their own privacy policies.</p>

    <h2>How long we keep it</h2>
    <p>Your board entry and account stay until you delete them. Reports are deleted once reviewed,
      within 90 days. After you delete your account, copies in our provider's backups are erased
      on its normal schedule (Google states up to 180 days).</p>

    <h2>Your rights</h2>
    <p>You can delete your account and board entry at any time in the game: open the menu, tap the
      person button, then <strong>Delete my account</strong>. You can also ask us by email (see
      <a href="delete-account.html">Delete your account</a>). Under the GDPR you also have the right
      to access, correct, restrict or object to the processing of your data, and to receive it in a
      portable form; write to <a href="mailto:{EMAIL}">{EMAIL}</a> and we answer within one month.
      You can complain to the data protection authority where you live or work.</p>

    <h2>Children</h2>
    <p>Skyframe is meant for players 13 and older. We do not knowingly collect data from children
      under 13; if you believe a child has saved a score, write to us and we will delete it.</p>

    <h2>Cookies and browser storage</h2>
    <p>The web version stores your progress and, if you save a score, your Firebase session in
      your browser's storage. This is strictly necessary for the features you use; there are no
      advertising or analytics cookies.</p>

    <h2>Changes</h2>
    <p>If this policy changes, the new version is posted here with a new date.</p>
"""

TERMS = f"""
    <p>By playing Skyframe and, in particular, by saving a score to the World board, you agree to
      these terms. If you don't agree, you can still play without saving scores online.</p>

    <h2>The game</h2>
    <p>Skyframe is free. It is provided "as is", without warranties of any kind, to the extent the
      law allows. We may change or end the game or the World board at any time.</p>

    <h2>Names on the World board</h2>
    <p>Names you choose are shown publicly next to your score and flag. A name must not:</p>
    <ul>
      <li>be offensive, hateful, sexual, violent or harassing;</li>
      <li>target a person or group because of who they are;</li>
      <li>include personal information such as a full name, phone number or address;</li>
      <li>impersonate another person, brand or Skyframe itself;</li>
      <li>advertise anything or include links.</li>
    </ul>
    <p>The game filters common offensive words. Any player can report a name or hide a player from
      their own view of the board.</p>

    <h2>Moderation</h2>
    <p>We review reported names and may, without notice, remove a name or an entry, or block an
      account from the board, if it breaks these rules or if a score looks impossible. If we remove
      something of yours you can write to us to ask why and to contest it.</p>

    <h2>Your account</h2>
    <p>You can delete your online account and board entry at any time; see
      <a href="delete-account.html">Delete your account</a>. How we handle your data is described in
      the <a href="index.html">Privacy policy</a>.</p>

    <h2>Liability</h2>
    <p>To the extent the law allows, Skyframe is not liable for any indirect or consequential loss
      arising from the game. Nothing in these terms limits rights you have as a consumer under the
      law of your country.</p>

    <h2>Contact and reports</h2>
    <p>Questions, reports and legal notices: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

DELETE = f"""
    <p>This page explains how to delete your Skyframe account and the data that goes with it. It
      applies to the game on iPhone and iPad (App Store), Android (Google Play) and the web.</p>

    <h2>In the game (fastest)</h2>
    <ol>
      <li>Open Skyframe and go to the main menu.</li>
      <li>Tap the person button, next to the sound button.</li>
      <li>Tap <strong>Delete my account</strong>, then confirm. If you signed in with Apple or
        Google, you are asked to sign in once more to confirm it's you.</li>
    </ol>
    <p>Deletion is immediate.</p>

    <h2>Without the game</h2>
    <p>Email <a href="mailto:{EMAIL}?subject=Delete%20my%20Skyframe%20account">{EMAIL}</a> with the
      subject "Delete my Skyframe account" and include your <strong>player ID</strong> (shown in the
      game under the person button) or, if you no longer have the game, your board name, flag,
      score and roughly when you saved it. We delete the account within 30 days and confirm by
      email.</p>

    <h2>What is deleted</h2>
    <ul>
      <li>Your online account (guest, Apple or Google sign-in), and for Apple, the game's access
        to your Apple ID is revoked;</li>
      <li>your entry on the World board: name, flag, score and its details;</li>
      <li>any reports filed about your name.</li>
    </ul>
    <h2>What is kept</h2>
    <p>Nothing on our side. Copies in our provider's (Google Firebase) backups are erased on its
      normal schedule, within 180 days. Progress saved on your device stays there until you
      uninstall the game or clear the site's data.</p>
"""

ACCESSIBILITY = f"""
    <p>We want Skyframe to be playable by as many people as possible. We aim to meet the Web
      Content Accessibility Guidelines (WCAG) 2.2, level AA, wherever the nature of a timed puzzle
      game allows it.</p>

    <h2>What the game supports</h2>
    <ul>
      <li>Screen readers: buttons, menus and game status (stage, time left, gaps below the line)
        have labels for VoiceOver, TalkBack and desktop screen readers.</li>
      <li>Every action works with on-screen buttons as well as gestures, and on the web with a
        keyboard alone.</li>
      <li>Reduced motion: when your device asks for less motion, the web version stops the camera
        push, the shake and the background motion, and the apps calm their animations.</li>
      <li>Colour is never the only signal: gaps below the line are outlined and counted in text.</li>
      <li>Sound and music can be turned off; nothing depends on hearing.</li>
      <li>Two looks (Golden Hour and Night Shift) and eight languages, including right-to-left
        Hebrew and Arabic.</li>
    </ul>

    <h2>Known limitations</h2>
    <ul>
      <li>The game is played against a clock, and the time limits can't be turned off: they are
        the game.</li>
      <li>In the iPhone, iPad and Android apps, text keeps its own size rather than following the
        system text size, so that the game screen stays legible on every phone.</li>
      <li>Placing falling blocks relies on seeing the board; it is not playable by screen reader
        alone.</li>
    </ul>

    <h2>Feedback</h2>
    <p>If something in Skyframe is hard to use, tell us at
      <a href="mailto:{EMAIL}?subject=Skyframe%20accessibility">{EMAIL}</a>. We answer within 14
      days. This statement was prepared on {UPDATED} and is reviewed with each major update.</p>
"""

SUPPORT = f"""
    <p>Need help with Skyframe, found a bug, or want to report a name on the World board? Write to
      <a href="mailto:{EMAIL}?subject=Skyframe">{EMAIL}</a>. We usually answer within a few days.</p>

    <h2>Common questions</h2>
    <h3>Do I need an account?</h3>
    <p>No. You can play without one. Saving a score to the World board makes a guest account for
      your device; on iPhone and iPad you can sign in with Apple, and on Android with Google, to
      keep your entry when you change phones.</p>
    <h3>How do I change my name or flag?</h3>
    <p>In the main menu, tap the person button, edit the name or tap the flag, then Save.</p>
    <h3>How do I report or hide a player?</h3>
    <p>On the World board, tap ⋯ next to their name.</p>
    <h3>How do I delete my account?</h3>
    <p>See <a href="delete-account.html">Delete your account</a>.</p>
"""

for filename, title in PAGES:
    body = {
        "index.html": PRIVACY,
        "terms.html": TERMS,
        "delete-account.html": DELETE,
        "accessibility.html": ACCESSIBILITY,
        "support.html": SUPPORT,
    }[filename]
    with open(filename, "w") as f:
        f.write(page(filename, title, body))
print("built", len(PAGES), "pages")
