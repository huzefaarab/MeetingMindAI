# Product Sync — Sprint 14 Review

**Date:** August 5, 2026
**Attendees:** John (Backend Lead), Sarah (DevOps), Mike (QA Lead), Emily (Marketing), David (Product Manager)
**Duration:** 42 minutes

---

David:
Alright, let's get started. We've got four things on the agenda today — auth, deployment, QA sign-off, and the marketing timeline for the launch. John, can you kick us off with where authentication landed?

John:
Sure. So the OAuth2 migration is basically done on the backend. We moved off the old session-token system entirely and we're now issuing short-lived JWTs with a fifteen-minute expiry plus a refresh token that's valid for seven days.

The tricky part was the refresh token rotation. If we don't rotate them on every use, a leaked refresh token stays valid until it expires naturally, which is a bad window. So now every time a refresh token is used, we invalidate it and issue a new one. That closes most of the replay attack surface.

One thing I want to flag — we're still using RS256 for signing, not HS256, because we've got multiple services that need to verify tokens independently without sharing a secret. That decision adds a little latency but it's the right call for a distributed setup like ours.

David:
Good. Any blockers on that side?

John:
Just one. We need Sarah's team to rotate the signing keys in the production secrets manager before we can cut over, since right now we're still validating against the old keys in staging.

---

Sarah:
Yeah, I saw that ticket. We can do the key rotation this week, probably Wednesday. That actually ties into what I wanted to cover for deployment.

We're moving the whole stack to blue-green deployment starting next sprint. Right now our rollback process is way too manual — if a deploy goes bad, someone has to SSH in and manually redirect traffic, and that's taken us almost twenty minutes in the last two incidents. With blue-green, we just flip the load balancer target group and rollback becomes instant.

The other big piece is we're finally containerizing the worker processes. They've been running as bare processes on EC2 this whole time, which means scaling them means manually spinning up new instances. Once they're in containers we can just let the autoscaler handle it based on queue depth.

David:
What's the timeline on containerizing the workers?

Sarah:
Two weeks, realistically. The Dockerfiles are mostly written already, the harder part is making sure the MQTT connections don't drop during a container restart, since we've got IoT devices publishing to those queues pretty much constantly and we can't afford to lose messages during a redeploy.

---

Mike:
I can jump in here since QA touches both of those. On the auth side, we've run about 200 test cases against the new JWT flow — token expiry, refresh rotation, revocation, and the concurrent-session edge cases. All passing except one: if a user has the app open on two devices and revokes a session from device A, device B doesn't get logged out until its access token naturally expires, which can be up to fifteen minutes.

John:
That's expected behavior for now, we're not doing push-based revocation yet. That would need a socket connection or polling, and we decided it's out of scope for this sprint.

Mike:
Okay, that's fine, I just wanted it documented so it doesn't get filed as a bug later.

For deployment, we haven't been able to test the blue-green rollback yet since it's not built, but I've already drafted the test plan — mainly focused on making sure in-flight requests don't get dropped during the traffic switch, and that database migrations that ran during the "green" deploy are safe to roll back if we revert to "blue."

David:
That's a good callout, actually. Sarah, are migrations reversible in the new pipeline?

Sarah:
Not automatically. We'd need every migration to ship with a down-migration, which isn't something we've enforced historically. I'll bring that up with the team, it might need to be a hard requirement going forward.

---

Emily:
So from the marketing side, we're targeting the public launch for September 15th, which is about six weeks out. That's built around the assumption that auth and the deployment pipeline are both stable by end of this month.

The campaign itself is going to lean heavily on the "switch accounts without re-logging-in" story, since that's actually a customer pain point we've heard about a lot in support tickets. So if there's any chance the multi-device revocation delay Mike mentioned becomes visible to users, I need to know now, because it directly contradicts the messaging.

John:
It shouldn't be visible in the common case — a user revoking their own session from a settings page and then panicking that another device is still logged in for a few minutes is an edge case, not the main flow.

Emily:
Okay, good, that's reassuring. Second thing — we want to do a soft-launch to about five percent of users on September 1st to catch anything before the full push. Is that feasible given where the deployment work is at?

Sarah:
Should be. Blue-green will be live by then, so a five percent rollout is actually a good first real-world test of the whole pipeline before we go wider.

David:
Great, let's lock that in. Soft launch September 1st, full launch September 15th, contingent on Mike's team giving sign-off on both auth and deployment by August 25th.

---

David:
Okay, let's wrap up with action items.

John:
I'll get the RS256 key rotation ticket over to Sarah's team today, and I'll write up the revocation-delay behavior in the docs so it's clear that's intentional, not a bug.

Sarah:
I'll rotate the signing keys by Wednesday, and start on the worker containerization this week. I'll also raise the down-migration requirement with the team and get a decision by Friday.

Mike:
I'll finish the blue-green test plan by early next week, and I'll keep running regression on the auth flow as John ships the remaining edge-case fixes.

Emily:
I'll get the soft-launch messaging drafted and share it for review, and I'll hold off finalizing the "seamless multi-device" campaign copy until Mike confirms sign-off on the revocation behavior.

David:
Perfect. Let's reconvene next Tuesday for a check-in before the August 25th sign-off deadline. Thanks, everyone.
