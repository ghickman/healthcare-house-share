var gulp = require('gulp');

var jshint = require('gulp-jshint');

var changed = require('gulp-changed');

var imagemin = require('gulp-imagemin');

var minifyHTML = require('gulp-minify-html');

var concat = require('gulp-concat');

var stripDebug = require('gulp-strip-debug');

var uglify = require('gulp-uglify');

var autoprefix = require('gulp-autoprefixer');

var minifyCSS = require('gulp-minify-css');

var notify = require('gulp-notify');

var sass = require('gulp-sass');

var coffee = require('gulp-coffee');

var gutil = require('gulp-util');

var devLocation = "hhs/devassets/";

var publishedLocation = "static/";

gulp.task('jshint', function(){
	gulp.src(devLocation+'js/*.js')
		.pipe(jshint())
		.pipe(jshint.reporter('default'));
});

// minify new images

gulp.task('imagemin', function(){
	var imgSrc = devLocation+'img/**/*',
	imgDst = publishedLocation+'img';

	gulp.src(imgSrc)
		.pipe(changed(imgDst))
		.pipe(imagemin())
		.pipe(gulp.dest(imgDst));
})

// minify new or changed html

gulp.task('htmlpage', function(){
	var htmlSrc = devLocation+'*.html',
	htmlDst = 'publishedLocation';

	gulp.src(htmlSrc)
		.pipe(changed(htmlDst))
		.pipe(minifyHTML())
		.pipe(gulp.dest(htmlDst));
})

// JS concat, strip debugging and minify

gulp.task('scripts', function(){
	gulp.src([devLocation+'js/vendor/*.js'])
		.pipe(concat('vendor.js'))
		.pipe(stripDebug())
		.pipe(uglify())
		.pipe(gulp.dest(publishedLocation+'js/'))
});

gulp.task('coffee', function() {
	gulp.src(devLocation+'js/*.coffee')
		.pipe(coffee({bare: true}).on('error', gutil.log))
		.pipe(gulp.dest(publishedLocation+'js/'));
});

// css concat, autoprefix, minify

gulp.task('styles', function(){
	gulp.src([devLocation+'css/*.css'])
		.pipe(concat('css.css'))
		.pipe(autoprefix('last 5 versions'))
		.pipe(minifyCSS())
		.pipe(gulp.dest(publishedLocation+'css/'))
		.pipe(notify('gulp complete'));
});

gulp.task('sass', function () {
	gulp.src(devLocation+'css/core.scss')
	.pipe(sass().on('error', sass.logError))
	.pipe(minifyCSS())
	.pipe(gulp.dest(publishedLocation+'css/'))
	.pipe(notify('gulp complete'));
});

gulp.task('fonts', function(){
	return gulp.src([devLocation+'fonts/**/**.*'])
		.pipe(gulp.dest(publishedLocation+'fonts/'));
})


// default gulp task

gulp.task('publish', ['imagemin', 'htmlpage', 'coffee', 'scripts','sass', 'fonts']);

gulp.task('default', function() {
	gulp.watch([devLocation+'css/**/*.scss', devLocation+'js/*.coffee' , devLocation+'*.html'], ['publish']);
});