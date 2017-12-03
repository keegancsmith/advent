;;; advent.el --- Advent of Code helpers

;; Author: Keegan Carruthers-Smith

;;; Commentary:

;; Simple adventofcode.com helper which downloads todays input as well as open
;; todays question.
;;
;; Ensure you have logged in with advent-login.  Once logged in, just call the
;; function advent.

;;; Code:

(require 'url)

(defvar advent-dir
  (expand-file-name "~/src/advent")
  "The directory you are doing advent of code in.")

(defun advent-login (session)
  "Login to adventofcode.com.
Argument SESSION session cookie value."
  (interactive "sValue of session cookie from logged in browser: ")
  (url-cookie-store "session" session "Thu, 25 Dec 2027 20:17:36 -0000" ".adventofcode.com" "/" nil))

(defun advent (&optional day)
  "Load todays adventofcode.com problem and input.
Optional argument DAY Load this day instead.  Defaults to today."
  (interactive)
  (let ((day (or day (advent-day))))
    (delete-other-windows)
    (split-window-right)
    (eww (format "http://adventofcode.com/2017/day/%d" day))
    (advent-input day)))

(defun advent-input (&optional day)
  "Load todays adventofcode.com input in other window.
Optional argument DAY Load this day instead.  Defaults to today."
  (interactive)
  (let* ((day (or day (advent-day)))
         (url (format "http://adventofcode.com/2017/day/%d/input" day))
         (dir (format "%s/2017/%d" (expand-file-name advent-dir) day))
         (file (format "%s/input" dir)))
    (if (not (file-exists-p file))
        (url-retrieve url 'advent-download-callback (list file))
      (find-file-other-window file))))

(defun advent-download-callback (status file)
  (if (plist-get status :error)
      (message "Failed to download todays advent %s" (plist-get status :error))
    (mkdir (file-name-directory file) t)
    (goto-char (point-min))
    (re-search-forward "\r?\n\r?\n")
    (write-region (point) (point-max) file)
    (find-file-other-window file)))

(defun advent-day ()
  (elt (decode-time (current-time)) 3))

;;; advent.el ends here
