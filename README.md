# QE-C Backlog Status

**Latest Run:** 2022-02-18 10:33:36 GMT
*(Please refresh to see latest results)*

This is the dashboard for Quality Engineering for Containers and Public Cloud.

We are currently working on four projects: Containers, JeOS, WSL, Public Cloud and SLE Micro
* [General team overview](#general_team_overview)
  * [Bugs vs Features Backlog Length](#bugs_vs_features_backlog_length)
  * [Incoming vs outcoming during the last 30 days](#incoming_vs_outcoming_during_the_last_30_days)
  * [Incoming vs outcoming during the last 4 months](#incoming_vs_outcoming_during_the_last_4_months)
* [Backlog Lengths by priority](#backlog_lengths_by_priority)
* [Pickup time alerts](#pickup_time_alerts)
* [Non updated tickets for 15 days](#non_updated_tickets_for_15_days)
  * [Tickets in progress with no changes in 15 days](#tickets_in_progress_with_no_changes_in_15_days)
  * [Tickets with the status Blocked and Feedback with no changes in 15 days](#tickets_with_the_status_blocked_and_feedback_with_no_changes_in_15_days)
* [No Changes in 15 Days (Blocked and Feedback)](#no_changes_in_15_days_blocked_and_feedback)
* [Abnormalities](#abnormalities)
  * [In Progress But Not Assigned](#in_progress_but_not_assigned)
  * [Assigned but not started](#assigned_but_not_started)
  * [New tickets](#new_tickets)
  * [Coordination without subtasks](#coordination_without_subtasks)
* [Epics](#epics)

# General team overview <a name='general_team_overview'></a>
**Bugs vs Features Backlog Length <a name='bugs_vs_features_backlog_length'></a>**

This table compares the number of bugs against the planned tickets.          

Project | Bugs | Features | Total
--- | --- | --- | ---
 | Containers | [ 4 (13%) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 27 (87%) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 31 ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)
 | JeOS | [ 7 (32%) ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 15 (68%) ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 22 ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)
 | WSL | [ 1 (17%) ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 5 (83%) ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 6 ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)
 | Public Cloud | [ 15 (32%) ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 32 (68%) ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 47 ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)
 | SLE Micro | [ 1 (6%) ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%3D&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 17 (94%) ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=priority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=issue_tags&op%5Bissue_tags%5D=%21&v%5Bissue_tags%5D%5B%5D=bug&f%5B%5D=&c%5B%5D=subject&c%5B%5D=project&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=relations&c%5B%5D=parent&c%5B%5D=tags_relations&c%5B%5D=updated_on&group_by=status&t%5B%5D=) | [ 18 ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&v%5Bstatus_id%5D%5B%5D=2&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=)


**Incoming vs outcoming during the last 30 days <a name='incoming_vs_outcoming_during_the_last_30_days'></a>**

This table shows the balance between ticket creation and ticket resolution. 
If more tickets arrive than we are capable of solving, 
it means that the length of the backlog will grow, and therefore we need more work force in that project. 
And more tickets come out than come in, so we can divert workforce to other projects if necessary.
Two time ranges are contemplated, short-term (30 days) and medium-term (4 months)

Backlog Query | New tickets | Finished tickets | Backlog length | Status
--- | --- | --- | --- | ---
 | Containers | 11 | 3 | 31 | &#x1F534;
 | JeOS | 7 | 14 | 22 | &#x1F49A;
 | WSL | 1 | 1 | 6 | &#x1F49A;
 | Public Cloud | 41 | 26 | 47 | &#x1F534;
 | SLE Micro | 17 | 6 | 18 | &#x1F534;


**Incoming vs outcoming during the last 4 months <a name='incoming_vs_outcoming_during_the_last_4_months'></a>**

Backlog Query | New tickets | Finished tickets | Backlog length | Status
--- | --- | --- | --- | ---
 | Containers | 50 | 62 | 31 | &#x1F49A;
 | JeOS | 19 | 20 | 22 | &#x1F49A;
 | WSL | 3 | 3 | 6 | &#x1F49A;
 | Public Cloud | 82 | 71 | 47 | &#x1F534;
 | SLE Micro | 21 | 6 | 18 | &#x1F534;



# Backlog Lengths by priority <a name='backlog_lengths_by_priority'></a>
These tables show the backlog length per priority. The "Warning level" is a the max number of tickets that we consider safe. This level is established by consensus in the team.

**Containers <a name='containers'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 3 | &#x1F49A;
 | [ Normal Priority Length: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 5 | 20 | &#x1F49A;


**JeOS <a name='jeos'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: JeOS ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: JeOS ](https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 3 | &#x1F49A;
 | [ Normal Priority Length: JeOS ](https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 5 | 20 | &#x1F49A;


**WSL <a name='wsl'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 3 | &#x1F49A;
 | [ Normal Priority Length: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 2 | 20 | &#x1F49A;


**SLE Micro <a name='sle_micro'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 3 | &#x1F49A;
 | [ Normal Priority Length: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 10 | 20 | &#x1F49A;


**Public Cloud <a name='public_cloud'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 1 | &#x1F49A;
 | [ High Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 3 | &#x1F49A;
 | [ Normal Priority Length: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 20 | 20 | &#x1F49A;



# Pickup time alerts <a name='pickup_time_alerts'></a>
These tables show the tickets that are in violation of the [SLO](https://progress.opensuse.org/projects/openqatests/wiki#SLOs-service-level-objectives)

**Urgent Priority <a name='urgent_priority'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Urgent Priority: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Urgent Priority: JeOS ](https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Urgent Priority: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Urgent Priority: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Urgent Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=6&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=7&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;


**High Priority <a name='high_priority'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ High Priority: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ High Priority: JeOS ](https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ High Priority: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 0 | &#x1F534;
 | [ High Priority: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ High Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=5&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=30&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;


**Normal Priority <a name='normal_priority'></a>**

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Normal Priority: Containers ](https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Normal Priority: JeOS ](https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Normal Priority: SLE Micro ](https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Normal Priority: WSL ](https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Normal Priority: Public Cloud ](https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=priority_id&op%5Bpriority_id%5D=%3D&v%5Bpriority_id%5D%5B%5D=4&f%5B%5D=created_on&op%5Bcreated_on%5D=%3Ct-&v%5Bcreated_on%5D%5B%5D=365&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;



# Non updated tickets for 15 days <a name='non_updated_tickets_for_15_days'></a>
These tables show the tickets that have more than 15 days without any update

**Tickets in progress with no changes in 15 days <a name='tickets_in_progress_with_no_changes_in_15_days'></a>**

These tickets are in progress and we should review that because maybe have blockers or are under feedback and we forgot to update the status of the ticket.

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Not Changed: Containers ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: JeOS ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: SLE Micro ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: WSL ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 2 | 0 | &#x1F534;


**Tickets with the status Blocked and Feedback with no changes in 15 days <a name='tickets_with_the_status_blocked_and_feedback_with_no_changes_in_15_days'></a>**

These tickets are in progress and we should review that because maybe what is blocking is solved. Or we need to insist when we don't have feedback.

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Not Changed: Containers (Blocked and Feedback) ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 3 | 0 | &#x1F534;
 | [ Not Changed: JeOS (Blocked and Feedback) ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 0 | &#x1F534;
 | [ Not Changed: SLE Micro (Blocked and Feedback) ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: WSL (Blocked and Feedback) ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Changed: Public Cloud (Blocked and Feedback) ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=15&v%5Bstatus_id%5D%5B%5D=4&f%5B%5D=updated_on&op%5Bupdated_on%5D=%3Ct-&v%5Bupdated_on%5D%5B%5D=15&f%5B%5D=priority_id&op%5Bpriority_id%5D=%21&v%5Bpriority_id%5D%5B%5D=3&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 3 | 0 | &#x1F534;



# Abnormalities <a name='abnormalities'></a>
These tickets has some kind of abnormality, and should be alerted to the team and reviewed

**In Progress But Not Assigned <a name='in_progress_but_not_assigned'></a>**

These are the typical tickets that due to forgetfulness are in progress but there is no assigned person. 
If there is any clarification to be made with the person who is working with it, we need to know his name

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Not Assigned: Containers ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Assigned: JeOS ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Assigned: SLE Micro ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Assigned: WSL ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Not Assigned: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=2&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%21*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;


**Assigned but not started <a name='assigned_but_not_started'></a>**

Some tickets could be blocked by a teammate for a time assigned to him but not started. This option is considered, 
but care must be taken if too much time has passed or if the person is on sick leave or on vacation. 
This would mean that the task is effectively blocked

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Assigned but not started: Containers ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Assigned but not started: JeOS ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Assigned but not started: SLE Micro ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Assigned but not started: WSL ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Assigned but not started: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=12&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=*&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;


**New tickets <a name='new_tickets'></a>**

New tickets that are not workable and need clarification should be reviewed during the refinement meeting.

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ New: Containers ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 0 | &#x1F534;
 | [ New: JeOS ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 8 | 0 | &#x1F534;
 | [ New: SLE Micro ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ New: WSL ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 0 | &#x1F534;
 | [ New: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=%3D&v%5Bstatus_id%5D%5B%5D=1&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=4&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 1 | 0 | &#x1F534;


**Coordination without subtasks <a name='coordination_without_subtasks'></a>**

Epics can be defined to record a new line of work in a project. 
Initially these epics may not have tasks assigned to them. This table is a reminder for the PO

Backlog Query | Number of issues | Warning level | Status
--- | --- | --- | ---
 | [ Coordination with no subtasks: Containers ]( https://progress.opensuse.org/projects/containers/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Coordination with no subtasks: JeOS ]( https://progress.opensuse.org/projects/jeos/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Coordination with no subtasks: SLE Micro ]( https://progress.opensuse.org/projects/microos_slemicro/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Coordination with no subtasks: WSL ]( https://progress.opensuse.org/projects/wsl/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;
 | [ Coordination with no subtasks: Public Cloud ]( https://progress.opensuse.org/projects/public_cloud/issues?utf8=%E2%9C%93&set_filter=1&sort=updated_on%2Cpriority%3Adesc%2Cid%3Adesc&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=6&f%5B%5D=child_id&op%5Bchild_id%5D=%21*&f%5B%5D=status_id&op%5Bstatus_id%5D=%21&v%5Bstatus_id%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D=3&v%5Bstatus_id%5D%5B%5D=5&v%5Bstatus_id%5D%5B%5D=6&f%5B%5D=&c%5B%5D=subject&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=author&c%5B%5D=assigned_to&c%5B%5D=created_on&c%5B%5D=relations&c%5B%5D=updated_on&c%5B%5D=project&group_by=status&t%5B%5D=) | 0 | 0 | &#x1F49A;



# Epics <a name='epics'></a>
**Container Epics <a name='container_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ New tests for SLE 15-SP4 / Leap 15.4](https://progress.opensuse.org/issues/105906) | Workable | 2022-02-03 | 35%
 | [ Enable test & release process on the container bo...](https://progress.opensuse.org/issues/104274) | Workable | 2022-01-31 | 0%
 | [ BCI testing](https://progress.opensuse.org/issues/103323) | Workable | 2021-09-05 | 25%
 | [ Test images on the container engines of the Publi...](https://progress.opensuse.org/issues/97553) | Workable | 2021-08-30 | 78%
 | [ Refactor container tests](https://progress.opensuse.org/issues/90086) | In Progress | 2021-01-28 | 87%
 | [{brainstorming}](https://progress.opensuse.org/issues/87853) | New | 2020-11-05 | 33%


**JeOS Epics <a name='jeos_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ Image oriented testing](https://progress.opensuse.org/issues/95428) | Workable | 2020-05-19 | 0%
 | [ {svirt} separate hyperv from svirt backend](https://progress.opensuse.org/issues/95422) | New | 2021-07-13 | 0%


**SLE Micro Epics <a name='sle_micro_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ Extend virtualization tests for MicroOS / SLE Micro ](https://progress.opensuse.org/issues/105133) | Workable | 2021-12-22 | 0%
 | [ New tests for SLE Micro version 5.2 ](https://progress.opensuse.org/issues/105130) | Workable | 2021-02-01 | 38%
 | [ Test SLE Micro on Public Cloud providers](https://progress.opensuse.org/issues/92794) | Workable | 2022-02-09 | 0%
 | [ Basic Cockpit UI testing on SLE Micro](https://progress.opensuse.org/issues/88393) | Workable | 2021-06-03 | 17%


**WSL Epics <a name='wsl_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ Backend improvement to create tests for WSL2](https://progress.opensuse.org/issues/105139) | New | 2019-11-27 | 33%


**Public Cloud Epics <a name='public_cloud_epics'></a>**

Epic | Status | Start Date | Progress
--- | --- | --- | ---
 | [ Incidents job groups should be created for all ve...](https://progress.opensuse.org/issues/103686) | Workable | 2021-12-08 | 75%
 | [ Using S3 Bucket as storage for updates needs to b...](https://progress.opensuse.org/issues/102275) | Workable | 2022-02-03 | 0%
 | [ Test staging PC images](https://progress.opensuse.org/issues/89845) | Workable | 2021-03-10 | 80%


