<!DOCTYPE html>
<html>
    
<!-- Mirrored from dreamguys.co.in/smarthr/blue/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Sat, 13 Apr 2019 07:16:04 GMT -->
<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0">
        <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.png">
        <title>Dashboard</title>
		<link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="assets/css/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="assets/css/line-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="assets/plugins/morris/morris.css">
        <link rel="stylesheet" type="text/css" href="assets/css/style.css">
		<!--[if lt IE 9]>
			<script src="assets/js/html5shiv.min.js"></script>
			<script src="assets/js/respond.min.js"></script>
		<![endif]-->
    </head>
    <body>
		<?php include "./sidebar.html" ?>
        <div class="main-wrapper">
            <div class="header">
                <div class="header-left">
                    <a href="index.html" class="logo">
						<img src="assets/img/logo.png" width="40" height="40" alt="">
					</a>
                </div>
				<a id="toggle_btn" href="javascript:void(0);"><i class="la la-bars"></i></a>
                <div class="page-title-box pull-left">
					<h3>KIDSTER</h3>
                </div>
				<a id="mobile_btn" class="mobile_btn pull-left" href="#sidebar"><i class="fa fa-bars" aria-hidden="true"></i></a>
				<ul class="nav navbar-nav navbar-right user-menu pull-right">
					<li class="dropdown hidden-xs">
						<a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-bell-o"></i> <span class="badge bg-purple pull-right">3</span></a>
						<div class="dropdown-menu notifications">
							<div class="topnav-dropdown-header">
								<span>Notifications</span>
							</div>
							<div class="drop-scroll">
								<ul class="media-list">
									<li class="media notification-message">
										<a href="activities.html">
											<div class="media-left">
												<span class="avatar">
													<img alt="John Doe" src="assets/img/user.jpg" class="img-responsive img-circle">
												</span>
											</div>
											<div class="media-body">
												<p class="m-0 noti-details"><span class="noti-title">John Doe</span> added new task <span class="noti-title">Patient appointment booking</span></p>
												<p class="m-0"><span class="notification-time">4 mins ago</span></p>
											</div>
										</a>
									</li>
									<li class="media notification-message">
										<a href="activities.html">
											<div class="media-left">
												<span class="avatar">V</span>
											</div>
											<div class="media-body">
												<p class="m-0 noti-details"><span class="noti-title">Tarah Shropshire</span> changed the task name <span class="noti-title">Appointment booking with payment gateway</span></p>
												<p class="m-0"><span class="notification-time">6 mins ago</span></p>
											</div>
										</a>
									</li>
									<li class="media notification-message">
										<a href="activities.html">
											<div class="media-left">
												<span class="avatar">L</span>
											</div>
											<div class="media-body">
												<p class="m-0 noti-details"><span class="noti-title">Misty Tison</span> added <span class="noti-title">Domenic Houston</span> and <span class="noti-title">Claire Mapes</span> to project <span class="noti-title">Doctor available module</span></p>
												<p class="m-0"><span class="notification-time">8 mins ago</span></p>
											</div>
										</a>
									</li>
									<li class="media notification-message">
										<a href="activities.html">
											<div class="media-left">
												<span class="avatar">G</span>
											</div>
											<div class="media-body">
												<p class="m-0 noti-details"><span class="noti-title">Rolland Webber</span> completed task <span class="noti-title">Patient and Doctor video conferencing</span></p>
												<p class="m-0"><span class="notification-time">12 mins ago</span></p>
											</div>
										</a>
									</li>
									<li class="media notification-message">
										<a href="activities.html">
											<div class="media-left">
												<span class="avatar">V</span>
											</div>
											<div class="media-body">
												<p class="m-0 noti-details"><span class="noti-title">Bernardo Galaviz</span> added new task <span class="noti-title">Private chat module</span></p>
												<p class="m-0"><span class="notification-time">2 days ago</span></p>
											</div>
										</a>
									</li>
								</ul>
							</div>
							<div class="topnav-dropdown-footer">
								<a href="activities.html">View all Notifications</a>
							</div>
						</div>
					</li>
					<li class="dropdown hidden-xs">
						<a href="javascript:;" id="open_msg_box" class="hasnotifications"><i class="fa fa-comment-o"></i> <span class="badge bg-purple pull-right">8</span></a>
					</li>	
					<li class="dropdown">
						<a href="profile.html" class="dropdown-toggle user-link" data-toggle="dropdown" title="Admin">
							<span class="user-img"><img class="img-circle" src="assets/img/user.jpg" width="40" alt="Admin">
							<span class="status online"></span></span>
							<span>Admin</span>
							<i class="caret"></i>
						</a>
						<ul class="dropdown-menu">
							<li><a href="profile.html">My Profile</a></li>
							<li><a href="edit-profile.html">Edit Profile</a></li>
							<li><a href="settings.html">Settings</a></li>
							<li><a href="login.html">Logout</a></li>
						</ul>
					</li>
				</ul>
				<div class="dropdown mobile-user-menu pull-right">
					<a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
					<ul class="dropdown-menu pull-right">
						<li><a href="profile.html">My Profile</a></li>
						<li><a href="edit-profile.html">Edit Profile</a></li>
						<li><a href="settings.html">Settings</a></li>
						<li><a href="login.html">Logout</a></li>
					</ul>
				</div>
            </div>
            <div class="sidebar" id="sidebar">
    <div class="sidebar-inner slimscroll">
        <div id="sidebar-menu" class="sidebar-menu">
            <ul>
                <li class="active"> 
                    <a href="index.html"><i class="la la-dashboard"></i> <span>Dashboard</span></a>
                </li>
                <li> 
                    <a href="clients.html"><i class="la la-users"></i> <span>Clients</span></a>
                </li>
                <li> 
                    <a href="projects.html"><i class="la la-rocket"></i> <span>Projects</span></a>
                </li>
                
                <li class="submenu">
                    <a href="#"><i class="la la-money"></i> <span> Payroll </span> <span class="menu-arrow"></span></a>
                    <ul style="display: none;">
                        <li><a href="assets.html"> Assets </a></li>
                        <li><a href="salary-view.html"> Payslip </a></li>
                    </ul>
                </li>
				<li> 
					<a href="worksheet.html"><i class="la la-clock-o"></i> <span>Timing Sheet</span></a>
				</li>
                <li> 
                    <a href="tickets.html"><i class="la la-ticket"></i> <span>Tickets</span></a>
                </li>
                <li> 
                    <a href="events.html"><i class="la la-calendar"></i> <span>Events</span></a>
                </li>
                <li> 
                    <a href="chat.html"><i class="la la-comments"></i> <span>Chat</span> <span class="badge bg-primary pull-right">5</span></a>
                </li>
                <li> 
                    <a href="activities.html"><i class="la la-bell"></i> <span>Activities</span></a>
                </li>        
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</div>
            <div class="page-wrapper">
                <div class="content container-fluid">
					<div class="row">
						<div class="col-md-6 col-sm-6 col-lg-3">
							<div class="dash-widget clearfix card-box">
								<span class="dash-widget-icon"><i class="fa fa-cubes" aria-hidden="true"></i></span>
								<div class="dash-widget-info">
									<h3>112</h3>
									<span>Projects</span>
								</div>
							</div>
						</div>
						<div class="col-md-6 col-sm-6 col-lg-3">
							<div class="dash-widget clearfix card-box">
								<span class="dash-widget-icon"><i class="fa fa-usd" aria-hidden="true"></i></span>
								<div class="dash-widget-info">
									<h3>44</h3>
									<span>Clients</span>
								</div>
							</div>
						</div>
						<div class="col-md-6 col-sm-6 col-lg-3">
							<div class="dash-widget clearfix card-box">
								<span class="dash-widget-icon"><i class="fa fa-diamond"></i></span>
								<div class="dash-widget-info">
									<h3>37</h3>
									<span>Tasks</span>
								</div>
							</div>
						</div>
						<div class="col-md-6 col-sm-6 col-lg-3">
							<div class="dash-widget clearfix card-box">
								<span class="dash-widget-icon"><i class="fa fa-user" aria-hidden="true"></i></span>
								<div class="dash-widget-info">
									<h3>218</h3>
									<span>Employees</span>
								</div>
							</div>
						</div>
					</div>
					
					<div class="row">
						<div class="col-md-6">
							<div class="panel panel-table">
								<div class="panel-heading">
									<h3 class="panel-title">Clients</h3>
								</div>
								<div class="panel-body">
									<div class="table-responsive">
										<table class="table table-striped custom-table m-b-0">
											<thead>
												<tr>
													<th style="min-width:200px;">Name</th>
													<th>Email</th>
													<th>Status</th>
													<th class="text-right">Action</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td style="min-width:200px;">
														<a href="#" class="avatar">B</a>
														<h2><a href="client-profile.html">Barry Cuda <span>CEO</span></a></h2>
													</td>
													<td>barrycuda@example.com</td>
													<td>
														<div class="dropdown action-label">
															<a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-success"></i> Active <i class="caret"></i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
																<li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
															</ul>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<a class="avatar">T</a>
														<h2><a href="client-profile.html">Tressa Wexler <span>Manager</span></a></h2>
													</td>
													<td>tressawexler@example.com</td>
													<td>
														<div class="dropdown action-label">
															<a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-danger"></i> Inactive <i class="caret"></i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
																<li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
															</ul>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<a href="client-profile.html" class="avatar">R</a>
														<h2><a href="client-profile.html">Ruby Bartlett <span>CEO</span></a></h2>
													</td>
													<td>rubybartlett@example.com</td>
													<td>
														<div class="dropdown action-label">
															<a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-danger"></i> Inactive <i class="caret"></i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
																<li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
															</ul>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<a href="client-profile.html" class="avatar">M</a>
														<h2><a href="client-profile.html"> Misty Tison <span>CEO</span></a></h2>
													</td>
													<td>mistytison@example.com</td>
													<td>
														<div class="dropdown action-label">
															<a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-success"></i> Active <i class="caret"></i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
																<li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
															</ul>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<a href="client-profile.html" class="avatar">D</a>
														<h2><a href="client-profile.html"> Daniel Deacon <span>CEO</span></a></h2>
													</td>
													<td>danieldeacon@example.com</td>
													<td>
														<div class="dropdown action-label">
															<a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-danger"></i> Inactive <i class="caret"></i>
															</a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
																<li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
															</ul>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
											</tbody>
										</table>
									</div>
								</div>
								<div class="panel-footer">
									<a href="clients.html" class="text-primary">View all clients</a>
								</div>
							</div>
						</div>
						<div class="col-md-6">
							<div class="panel panel-table">
								<div class="panel-heading">
									<h3 class="panel-title">Recent Projects</h3>
								</div>
								<div class="panel-body">
									<div class="table-responsive">
										<table class="table table-striped custom-table m-b-0">
											<thead>
												<tr>
													<th class="col-md-3">Project Name </th>
													<th class="col-md-3">Progress</th>
													<th class="text-right col-md-1">Action</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>
														<h2><a href="project-view.html">Food and Drinks</a></h2>
														<small class="block text-ellipsis">
															<span class="text-xs">1</span> <span class="text-muted">open tasks, </span>
															<span class="text-xs">9</span> <span class="text-muted">tasks completed</span>
														</small>
													</td>
													<td>
														<div class="progress progress-xs progress-striped">
															<div class="progress-bar bg-success" role="progressbar" data-toggle="tooltip" title="65%" style="width: 65%"></div>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<h2><a href="project-view.html">School Guru</a></h2>
														<small class="block text-ellipsis">
															<span class="text-xs">2</span> <span class="text-muted">open tasks, </span>
															<span class="text-xs">5</span> <span class="text-muted">tasks completed</span>
														</small>
													</td>
													<td>
														<div class="progress progress-xs progress-striped">
															<div class="progress-bar bg-success" role="progressbar" data-toggle="tooltip" title="15%" style="width: 15%"></div>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<h2><a href="project-view.html">Penabook</a></h2>
														<small class="block text-ellipsis">
															<span class="text-xs">3</span> <span class="text-muted">open tasks, </span>
															<span class="text-xs">3</span> <span class="text-muted">tasks completed</span>
														</small>
													</td>
													<td>
														<div class="progress progress-xs progress-striped">
															<div class="progress-bar bg-success" role="progressbar" data-toggle="tooltip" title="49%" style="width: 49%"></div>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<h2><a href="project-view.html">Harvey Clinic</a></h2>
														<small class="block text-ellipsis">
															<span class="text-xs">12</span> <span class="text-muted">open tasks, </span>
															<span class="text-xs">4</span> <span class="text-muted">tasks completed</span>
														</small>
													</td>
													<td>
														<div class="progress progress-xs progress-striped">
															<div class="progress-bar bg-success" role="progressbar" data-toggle="tooltip" title="88%" style="width: 88%"></div>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
												<tr>
													<td>
														<h2><a href="project-view.html">The Gigs</a></h2>
														<small class="block text-ellipsis">
															<span class="text-xs">7</span> <span class="text-muted">open tasks, </span>
															<span class="text-xs">14</span> <span class="text-muted">tasks completed</span>
														</small>
													</td>
													<td>
														<div class="progress progress-xs progress-striped">
															<div class="progress-bar bg-success" role="progressbar" data-toggle="tooltip" title="100%" style="width: 100%"></div>
														</div>
													</td>
													<td class="text-right">
														<div class="dropdown">
															<a href="#" class="action-icon dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-ellipsis-v"></i></a>
															<ul class="dropdown-menu pull-right">
																<li><a href="#" title="Edit"><i class="fa fa-pencil m-r-5"></i> Edit</a></li>
																<li><a href="#" title="Delete"><i class="fa fa-trash-o m-r-5"></i> Delete</a></li>
															</ul>
														</div>
													</td>
												</tr>
											</tbody>
										</table>
									</div>
								</div>
								<div class="panel-footer">
									<a href="projects.html" class="text-primary">View all projects</a>
								</div>
							</div>
						</div>
					</div>
					<div class="themes">
						<div class="themes-icon"><i class="fa fa-cog"></i></div>
						<div class="themes-body">
							<ul id="theme-change" class="theme-colors">
								<li><a href="https://dreamguys.co.in/smarthr/orange/index.html"><span class="theme-orange"></span></a></li>
								<li><a href="https://dreamguys.co.in/smarthr/purple/index.html"><span class="theme-purple"></span></a></li> 
								<li><a href="index.html"><span class="theme-blue"></span></a></li>
								<li><a href="https://dreamguys.co.in/smarthr/maroon/index.html"><span class="theme-maroon"></span></a></li>
								<li><a href="https://dreamguys.co.in/smarthr/light/index.html"><span class="theme-light"></span></a></li> 
								<li><a href="https://dreamguys.co.in/smarthr/dark/index.html"><span class="theme-dark"></span></a></li> 
								<li><a href="https://dreamguys.co.in/smarthr/rtl/index.html"><span class="theme-rtl">RTL</span></a></li>
							</ul>
						</div>
					</div>
				</div>			
			</div>
        </div>
		<div class="sidebar-overlay" data-reff="#sidebar"></div>
        <script type="text/javascript" src="assets/js/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="assets/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="assets/js/jquery.slimscroll.js"></script>
		<script type="text/javascript" src="assets/plugins/morris/morris.min.js"></script>
		<script type="text/javascript" src="assets/plugins/raphael/raphael-min.js"></script>
		<script type="text/javascript" src="assets/js/app.js"></script>
		<script type="text/javascript" src="assets/js/chart.js"></script>
    </body>
</html>